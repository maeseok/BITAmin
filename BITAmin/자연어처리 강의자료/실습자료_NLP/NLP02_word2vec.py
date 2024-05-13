#1. Training Samples
import pandas as pd
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
data = pd.read_csv('transcripts.csv')
print('Missing Values: ', data.isnull().sum())
data = data.dropna().reset_index(drop=True)
merge_data = ''.join(str(data.iloc[i,0]) for i in range(100))
print('Total word count: ', len(merge_data))


tokenizer = RegexpTokenizer("[\w]+")
token_text = tokenizer.tokenize(merge_data)


stop_words = set(stopwords.words('english'))
token_stop_text = []
for w in token_text:
    if w not in stop_words:
        token_stop_text.append(w)
print('After cleaning :', len(token_stop_text))

word2inx = {}
Bow = []
for word in token_stop_text:
    if word not in word2inx.keys():
        word2inx[word] = len(word2inx)
        Bow.insert(len(word2inx)-1,1)
    else:
        inx = word2inx.get(word)
        Bow[inx] += 1
print('Unique Words Count :', len(Bow))
# word2inx This is the result of integer encoding

#2. Word2Vec Training
import numpy as np
token_stop_text = np.reshape(np.array(token_stop_text),[-1,1])
from gensim.models import Word2Vec
model = Word2Vec(vector_size = 100, window = 5, min_count = 2, sg = 0)
model.build_vocab(token_stop_text)
model.train(token_stop_text, total_examples = model.corpus_count, epochs = 30, report_delay = 1)
vocabs = model.wv.key_to_index.keys()
word_vec_list = [model.wv[i] for i in vocabs]


from sklearn.decomposition import PCA
pca = PCA(n_components = 2)
pcafit = pca.fit_transform(word_vec_list)
x = pcafit[0:50,0]
y = pcafit[0:50,1]
import matplotlib.pyplot as plt
plt.scatter(x, y, marker = 'o')
for i, v in enumerate(vocabs):
    if i <= 49:
        plt.annotate(v, xy = (x[i], y[i]))
plt.show()
# sg : kip-gram
# # vector_size : embedded vector size0 is CBOW, 1 is S
# window : context window size
# min_count : do not apply word2vec to sparse words