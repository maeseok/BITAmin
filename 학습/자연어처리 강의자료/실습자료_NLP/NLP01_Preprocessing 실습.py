
#1. 표준 토큰화

from nltk.tokenize import TreebankWordTokenizer
tokenizer = TreebankWordTokenizer()
text = "Model-based RL don't need a value function for the policy."
print(tokenizer.tokenize(text))

from nltk.tokenize import word_tokenize
print(word_tokenize(text))

from nltk.stem import PorterStemmer, LancasterStemmer
stem1 = PorterStemmer()
stem2 = LancasterStemmer()
words = ["eat", "ate", "eaten", "eating"]
print("Porter Stemmer   :", [stem1.stem(w) for w in words])
print("Lancaster Stemmer:", [stem2.stem(w) for w in words])


import nltk
from nltk import WordNetLemmatizer
nltk.download('wordnet')
lemm = WordNetLemmatizer()
words = ["eat", "ate", "eaten", "eating"]
print("WordNet Lemmatizer:",[lemm.lemmatize(w, pos="v") for w in words])



#2. 불용어 예시
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
print(stopwords.words('english')[:5])

#3. 토큰화 후 불용어 제거하기
import nltk
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

input_sentence = "We should all study hard for the exam."
stop_words = set(stopwords.words('english'))
word_tokens = word_tokenize(input_sentence)
result = []
for w in word_tokens:
    if w not in stop_words:
        result.append(w)
print(word_tokens)
print(result)

#4. Enumerate 사용법 예시
mylist = ['English', 'Math', 'Science']
for n, name in enumerate(mylist):
    print("Course : {}, Number : {}".format(name, n))


#5. 정수 인코딩 및 Sorting
vocab = {'apple': 2, 'July': 6, 'piano': 4, 'cup': 8, 'orange': 1}
vocab_sort = sorted(vocab.items(), key = lambda x:x[1], reverse = True)
print(vocab_sort)
word2inx = {word[0] : index + 1 for index, word in enumerate(vocab_sort)}
print(word2inx)

#6. BoW 만들기
from nltk.tokenize import TreebankWordTokenizer
tokenizer = TreebankWordTokenizer()
text = "Model-based RL don't need a value function for the policy, " \
       "but some of Model-based RL algorithms do have a value function."
token_text = tokenizer.tokenize(text)
word2inx = {}
Bow = []
for word in token_text:
    if word not in word2inx.keys():
        word2inx[word] = len(word2inx)
        Bow.insert(len(word2inx)-1,1)
    else:
        inx = word2inx.get(word)
        Bow[inx] += 1
print(word2inx)
print(Bow)

#7. Cosine similarity
import numpy as np
def cos_sim(A, B):
    return np.dot(A, B) / (np.linalg.norm(A)*np.linalg.norm(B))

a = [1,0,0,1]
b = [0,1,1,0]
c = [1,1,1,1]
print(cos_sim(a,b), cos_sim(b,c), cos_sim(c,a))

#8. Levenschtein distance
import numpy as np
def leven(text1, text2):
    len1 = len(text1) + 1
    len2 = len(text2) + 1
    sim_array = np.zeros((len1, len2))
    sim_array[:,0] = np.linspace(0, len1-1, len1)
    sim_array[0,:] = np.linspace(0, len2-1, len2)
    for i in range(1,len1):
        for j in range(1,len2):
            add_char = sim_array[i-1,j] + 1
            sub_char = sim_array[i,j-1] + 1
            if text1[i-1] == text2[j-1]:
                mod_char = sim_array[i-1,j-1]
            else:
                mod_char = sim_array[i-1,j-1] + 1
            sim_array[i,j] = min([add_char, sub_char, mod_char])
    return sim_array[-1,-1]
print(leven('데이터마이닝','데이타마닝'))