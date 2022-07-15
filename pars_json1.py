import json

max = 0
max_name = ''
max_lastname = ''
with open('manager_sales.json', 'r') as file:
    data = json.load(file)

    for element in data:
        name = element['manager']['first_name']
        lastname = element['manager']['last_name']
        total = 0

        for car in element['cars']:
            total += car['price']

        if total > max:
            max = total
            max_name = name
            max_lastname = lastname
    print(max_name, max_lastname, max)
