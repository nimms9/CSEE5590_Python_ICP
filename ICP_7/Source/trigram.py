import nltk
f = open('input.txt', 'r',encoding='utf-8')
input = f.read()
stokens = nltk.sent_tokenize(input)
wtokens = nltk.word_tokenize(input)
# trigram
from nltk.util import ngrams
trigram = ngrams(wtokens,3)
for i in trigram:
    print(i)