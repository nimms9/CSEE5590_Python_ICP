import nltk
f = open('input.txt', 'r',encoding='utf-8')
input = f.read()
stokens = nltk.sent_tokenize(input)
wtokens = nltk.word_tokenize(input)

for s in stokens:
    print(s)
print('--------------------------------------------------------------------------')
for t in wtokens:
    print(t)
