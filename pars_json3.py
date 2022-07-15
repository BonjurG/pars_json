import json

with open('Alphabet.json') as dict:
    d = json.load(dict)

with open('Abracadabra.txt') as text:
    t = text.read()

for i in t:
    if i in d:
        print(d[i], end='')
    else:
        print(i, end='')


#import json
#
#with open('Alphabet.json') as dict, open('Abracadabra.txt') as text:
#    d = json.load(dict)
#    t = text.read()
#
#for i in t:
#    if i in d:
#        print(d[i], end='')
#    else:
#        print(i, end='')