import json
with open("Studentdata.json","r") as file:
    data=json.load(file)
    print(data)