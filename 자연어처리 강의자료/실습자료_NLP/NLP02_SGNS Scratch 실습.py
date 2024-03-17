#SGNS
import pandas as pd
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import numpy as np
data = pd.read_csv('transcripts.csv')
print('Missing Values: ', data.isnull().sum())
data = data.dropna().reset_index(drop=True)
merge_data = ''.join(str(data.iloc[i,0]) for i in range(30))
print('Total word count: ', len(merge_data))

tokenizer = RegexpTokenizer("[\w]+")
token_text = tokenizer.tokenize(merge_data)

stop_words = set(stopwords.words('english'))
token_stop_text = []
for w in token_text:
    if w not in stop_words:
        token_stop_text.append(w)
print('After cleaning :', len(token_stop_text))

from tensorflow.keras.preprocessing.text import Tokenizer
tokenizer = Tokenizer()
tokenizer.fit_on_texts(token_stop_text)
word2idx = tokenizer.word_index
encoded = tokenizer.texts_to_sequences(token_stop_text)
encoded = np.array(encoded).T
from tensorflow.keras.preprocessing.sequence import skipgrams
skip_gram = [skipgrams(sample, vocabulary_size = len(word2idx)+1,
                       window_size = 10) for sample in encoded]


import torch
import torch.nn as nn
from torch import LongTensor as LT
from torch import FloatTensor as FT

class Word2Vec(nn.Module):
    def __init__(self, vocab_size, embed_size):
        super(Word2Vec, self).__init__()
        self.vocab_size = vocab_size
        self.embed_size = embed_size
        self.word1_vector = nn.Embedding(self.vocab_size, self.embed_size)
        self.word2_vector = nn.Embedding(self.vocab_size, self.embed_size)
        self.word1_vector.weight = \
            nn.Parameter(torch.cat([torch.zeros(1, self.embed_size), FT(self.vocab_size-1,
                                                                       self.embed_size).uniform_(-0.1, 0.1)]))
        self.word2_vector.weight = \
            nn.Parameter(torch.cat([torch.zeros(1, self.embed_size), FT(self.vocab_size - 1,
                                                                       self.embed_size).uniform_(-0.1, 0.1)]))
        self.word1_vector.weight.requires_grad = True
        self.word2_vector.weight.requires_grad = True

    def forward_word1(self, data):
        vec = LT(data)
        vec = vec.cuda() if self.word1_vector.weight.is_cuda else vec
        return self.word1_vector(vec)


    def forward_word2(self, data):
        vec = LT(data)
        vec = vec.cuda() if self.word2_vector.weight.is_cuda else vec
        return self.word2_vector(vec)

class SGNS(nn.Module):
    def __init__(self, embed, vocab_size):
        super(SGNS, self).__init__()
        self.embed = embed
        self.vocab_size = vocab_size
        self.weights = None
    def forward(self, word1, word2, label):
        word1 = self.embed.forward_word1(word1).unsqueeze(1)
        word2 = self.embed.forward_word2(word2).unsqueeze(2)
        label = LT(label).unsqueeze(1)
        prediction = torch.bmm(word1, word2).squeeze(2).sigmoid().log()
        loss = -label * prediction
        return loss.mean()

from torch.optim import Adam
from torch.utils.data import DataLoader, TensorDataset
from tqdm import tqdm
vocab_size = len(word2idx)+1
word2vec = Word2Vec(vocab_size = vocab_size, embed_size = 100)
sgns = SGNS(embed = word2vec, vocab_size = vocab_size)
optim = Adam(sgns.parameters())
print('Train Ready')


for _, element in enumerate(skip_gram):
    word1 = LT(np.array(list(zip(*element[0]))[0], dtype = 'int32'))
    word2 = LT(np.array(list(zip(*element[0]))[1], dtype = 'int32'))
    label = LT(np.array(element[1], dtype = 'int32'))
    dataset = TensorDataset(word1, word2, label)
    train_loader = DataLoader(dataset, batch_size = 256, shuffle = True)
print('Data Loaded')

for epoch in range(5):
    with tqdm(train_loader, unit = 'batch') as tepoch:
        for word1, word2, label in tepoch:
            loss = sgns(word1, word2, label)
            optim.zero_grad()
            loss.backward()
            optim.step()
            tepoch.set_description(f"Epoch {epoch}")
            tepoch.set_postfix(loss = loss.item())

f = open('vectors.txt' ,'w')
ww = 0
f.write('{} {}\n'.format(7930, 100))
vectors = word2vec.word1_vector.weight.detach().numpy()
for i, v in enumerate(word2idx.keys()):
    try:
        f.write('{} {}\n'.format(v, ' '.join(map(str, list(vectors[i+1, :])))))
        ww += 1
    except:
        print('Non-English Characters')
f.close()
import gensim
embed_word2vec = gensim.models.KeyedVectors.load_word2vec_format('vectors.txt', binary = False)

embed_word2vec.most_similar(positive = ['country'])

