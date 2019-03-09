import nltk
f = open('input.txt', 'r',encoding='utf-8')
input = f.read()
stokens = nltk.sent_tokenize(input)
wtokens = nltk.word_tokenize(input)
#PARTS OF SPEECH TAGGING
nltk.download('averaged_perceptron_tagger')
print(nltk.pos_tag(wtokens))