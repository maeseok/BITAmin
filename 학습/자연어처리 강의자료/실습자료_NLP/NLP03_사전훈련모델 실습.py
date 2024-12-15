import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
import re
from nltk.tokenize import RegexpTokenizer
import gensim.downloader as api
from sklearn.metrics.pairwise import cosine_similarity
from gensim.models.word2vec import Word2Vec
from gensim.models import KeyedVectors

data = pd.read_csv('pretrained_data.csv')
print('#of docs:', len(data))
print(data.head())
data['cleaned'] = data['Desc'].apply(lambda s: "".join(i for i in s if ord(i) < 128))
data['cleaned'] = data['cleaned'].apply(lambda s: s.lower())
stop = set(stopwords.words('english'))
data['cleaned'] = data['cleaned'].apply(lambda s: " ".join([w for w in s.split() if not w in stop]))
html_parser = re.compile('<.*?>')
data['cleaned'] = data['cleaned'].apply(lambda s: html_parser.sub(r'',s))
tokenizer = RegexpTokenizer(r'[a-zA-Z]+')
data['cleaned'] = data['cleaned'].apply(lambda s: " ".join(tokenizer.tokenize(s)))
print(data['cleaned'][:3])

data['cleaned'].replace('', np.nan, inplace = True)
data = data[data['cleaned'].notna()]
print('# of docs after cleaning: ', len(data))

corpus = []
for word in data['cleaned']:
    corpus.append(word.split())

word2vec_model = api.load('glove-wiki-gigaword-50')
#word2vec_model = Word2Vec(vector_size = 300, window = 5, min_count = 2, workers = -1)
#word2vec_model.build_vocab(corpus)
#word2vec_model.build_vocab([list(pre_model.index_to_key())], update = True)
#word2vec_model.intersect_word2vec_format('GoogleNews-vectors-negative300.bin', lockf = 1.0, binary = False)
#word2vec_model.train(corpus, total_examples = word2vec_model.corpus_count, epochs = 10)

def average_vector(doc_list):
    doc_embed_list = []
    for line in doc_list:
        doc2vec = None
        count = 0
        for word in line.split():
            if word in word2vec_model:
                count += 1
                if doc2vec is None:
                    doc2vec = word2vec_model[word]
                else:
                    doc2vec = doc2vec + word2vec_model[word]
        if doc2vec is not None:
            doc2vec = doc2vec / count
            doc_embed_list.append(doc2vec)
    return doc_embed_list

doc_embed_list = average_vector(data['cleaned'])
print('# of doc vec:',len(doc_embed_list))

cos_sim = cosine_similarity(doc_embed_list, doc_embed_list)

def recommend_book(title):
    books = data[['title']]
    indices = pd.Series(data.index, index = data['title']).drop_duplicates()
    idx = indices[title]
    sim_score = list(enumerate(cos_sim[idx]))
    sim_score = sorted(sim_score, key = lambda x: x[1], reverse = True)
    sim_score = sim_score[1:6]
    book_indices = [i[0] for i in sim_score]
    recommend = books.iloc[book_indices].reset_index(drop = True)
    for index, row in recommend.iterrows():
        print(index, row['title'])

recommend_book('The Da Vinci Code')

