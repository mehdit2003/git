import json

jsonfile = open('steam.json')

pythonfile = json.load(jsonfile)
items = 0

for i in pythonfile:
    items+=1

    print(items)