f1=open('nlp_input.txt','r')
text = f1.read()
#print(text)


from nltk.stem import WordNetLemmatizer
import nltk
nltk.download('wordnet')

wtokens = nltk.word_tokenize(text)

lemmatizer = WordNetLemmatizer()
print('--------------3(b) Lemmatization technique on each word---------------')
for wt in wtokens:

    print(lemmatizer.lemmatize(wt))

from nltk.util import ngrams
trigrams=ngrams(wtokens,3)
print('--------------3(c) All Trigrams for the words-------------')
for tri in trigrams:

    print(tri)

import collections
trigram_frequency = collections.Counter(trigrams)
top_10 = trigram_frequency.most_common(10)
print('--------------3(d)Top 10 Trigrams for the words-------------')
print(top_10)

l=[]
for i in top_10:
    l.append(i[0])


stokens = nltk.sent_tokenize(text)

s=[]
for i in stokens:
    for j in l:
        if j[0] in i and j[1] in i and j[2] in i:
            s.append(i)
print('--------------- sentences with top 10 trigrams -----------------')
print(s)

s1=''

for i in set(s):
    s1+=i
print('---------concatenated result-----------')
print(s1)