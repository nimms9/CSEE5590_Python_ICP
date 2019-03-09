from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer


f = open('input.txt', 'r',encoding='utf-8')
input = f.read()

pStemmer = PorterStemmer()
print(pStemmer.stem(input))

print('-----------------------------------------------------------------------------------------------')

lStemmer = LancasterStemmer()
print(lStemmer.stem(input))
