import nltk
from nltk import WordNetLemmatizer
f=open('input.txt','r',encoding='utf-8')
input = f.read()
#LEMMATIZATION
nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize(input))