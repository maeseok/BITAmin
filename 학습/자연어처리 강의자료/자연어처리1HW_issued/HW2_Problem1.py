

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch import LongTensor as LT
from torchtext.legacy import data

class lstm_net(nn.Module):
    def __init__(self, vocab_size, embed_size, hidden_size, out_size, num_layers, bidirectional = True):
        super(lstm_net, self).__init__()
        self.scaler = 2 if bidirectional == True else 1
        self.embed = nn.Embedding(vocab_size, embed_size)
        self.lstm = nn.LSTM(embed_size, hidden_size, num_layers = num_layers, bidirectional = bidirectional)
        self.fclayer = nn.Linear(hidden_size * self.scaler, hidden_size)
        self.fclayer2 = nn.Linear(hidden_size, out_size)

    def forward(self, text):
        embed = self.embed(text) # [len, batch, embed_dim]
        out, (hidden, cell) = self.lstm(embed)
        # out = [len, batch, hidden_size * scaler]
        # hidden = [num_layers * scaler, batch, hidden_size]
        if self.scaler == 1:
            return self.fclayer2(self.fclayer(hidden[-1,:,:]).relu())
        else:
            return self.fclayer2(self.fclayer(torch.cat((hidden[-2,:,:],hidden[-1,:,:]),dim=1)).relu())

text = data.Field(tokenize='spacy',tokenizer_language='en_core_web_sm',include_lengths=True)
label = data.LabelField(dtype=torch.float)

from torchtext.legacy import datasets
train_data, test_data = datasets.IMDB.splits(text, label)

text.build_vocab(train_data, max_size = 25000, vectors = 'glove.6B.100d', unk_init = torch.Tensor.normal_)
label.build_vocab(train_data)
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
train_iter, test_iter = data.BucketIterator.splits((train_data, test_data), batch_size = 256, sort_within_batch = True, device = device)
print(len(train_iter))
model = lstm_net(vocab_size = len(text.vocab), embed_size = 100, hidden_size = 64, out_size = 1, num_layers = 1, bidirectional = False)
print(text.vocab.vectors.shape)
model.embed.weight.data.copy_(text.vocab.vectors)
optimizer = torch.optim.Adam(model.parameters())
model = model.to(device)
loss_fcn = nn.BCEWithLogitsLoss()
loss_fcn = loss_fcn.to(device)
print('Start Training')
for epoch in range(5):
    epoch_loss = 0
    epoch_right = 0
    for minibatch in train_iter:
        text_, _ = minibatch.text
        pred = model.forward(text_).squeeze(1)
        loss = loss_fcn(pred, minibatch.label)
        right = (torch.round(torch.sigmoid(pred)) == minibatch.label).float().sum()
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        epoch_loss += loss.item()
        epoch_right += right.item()
    print('Epoch:',epoch,'Loss:',epoch_loss,'Correct:',epoch_right)

print('Test')
import spacy
nlp = spacy.load('en_core_web_sm')
tokenized = [tok.text for tok in nlp.tokenizer('This movie was horrible, never watch it again')]
index = [text.vocab.stoi[t] for t in tokenized]
tensor_test = LT(index).to(device).unsqueeze(1)
pred = torch.sigmoid(model(tensor_test))
print(pred.item())
