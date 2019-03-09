import nltk
f=open('input.txt','r',encoding='utf-8')
input = f.read()
#named entity recognition
nltk.download('maxent_ne_chunker')
nltk.download('words')
from nltk import wordpunct_tokenize, pos_tag, ne_chunk
print(ne_chunk(pos_tag(wordpunct_tokenize(input))))