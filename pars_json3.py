import json

with open('Alphabet.json') as dict_file:
    dict = json.load(dict_file)

with open('Abracadabra.txt') as text_file:
    text = text_file.read()

for i in text:
    if i in dict:
        print(dict[i], end='')
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