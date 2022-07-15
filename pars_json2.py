import json

with open('group_people.json', 'r') as file:
    data = json.load(file)
    maxi = 0
    max_gr = ''
    for element in data:
        ide = element['id_group']
        count = 0
        for person in element['people']:
            if person['gender'] == 'Female' and person['year'] > 1977:
                count += 1
        if count > maxi:
            maxi = count
            max_gr = ide
    print(maxi, max_gr)
