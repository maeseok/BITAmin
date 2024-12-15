import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch import LongTensor as LT
size_context = 3
dim_embedding = 10
num_epoch = 60
test_sentence = """The expression of his face as he said these words was not at all pleasant, and I had my own reasons for thinking that the stranger was mistaken, even supposing he meant what he said. But it was no affair of mine, I thought; and besides, it was difficult to know what to do. The stranger kept hanging about just inside the inn door, peering round the corner like a cat waiting for a mouse. Once I stepped out myself into the road, but he immediately called me back, and as I did not obey quick enough for his fancy, a most horrible change came over his tallowy face, and he ordered me in with an oath that made me jump. As soon as I was back again he returned to his former manner, half fawning, half sneering, patted me on the shoulder, told me I was a good boy and he had taken quite a fancy to me. I have a son of my own, said he, as like you as two blocks, and he's all the pride of my 'art. But the great thing for boys is discipline, sonny--discipline. Now, if you had sailed along of Bill, you wouldn't have stood there to be spoke to twice--not you. That was never Bill's way, nor the way of sich as sailed with him. And here, sure enough, is my mate Bill, with a spy-glass under his arm, bless his old 'art, to be sure. You and me'll just go back into the parlour, sonny, and get behind the door, and we'll give Bill a little surprise—bless his 'art, I say again.""".split()
ngram = [([test_sentence[i-j-1] for j in range(size_context)],test_sentence[i]) for i in range(size_context, len(test_sentence))]
print(ngram[:5])

vocab = set(test_sentence)
word_to_ix = {word: i for i, word in enumerate(vocab)}
print(word_to_ix)

class N_Gram_Embed(nn.Module):
    def __init__(self, size_vocab, dim_embedding, size_context, hidden_size = 64):
        super(N_Gram_Embed, self).__init__()
        """
        TODO
        """
    def forward(self, inputs):
        """
        TODO
        """
        return log_prob
loss_cul = []
loss_func = nn.NLLLoss()
model = N_Gram_Embed(len(vocab), dim_embedding, size_context)
optimizer = optim.SGD(model.parameters(), lr=1e-3)
for epoch in range(num_epoch):
    loss_epoch = 0
    for context, target in ngram:
        context_idx = LT([word_to_ix[w] for w in context])
        model.zero_grad()
        loss = loss_func(model.forward(context_idx), LT([word_to_ix[target]]))
        loss.backward()
        optimizer.step()
        loss_epoch += loss.item()
    loss_cul.append(loss_epoch)
    print("Epoch:",epoch,"Loss:",loss_epoch)
#TEST
print(model.embed.weight[word_to_ix["expression"]])