import json

students = [
    {"Name": "Alice", "Alter": 24},
    {"Name": "Benjamin", "Alter": 20},
    {"Name": "Ömer", "Alter": 29}
]

with open("students.json", 'w') as jsonFile:
    json.dump(students, jsonFile)

with open("students.json", 'r') as jsonFile:
    content = json.load(jsonFile)
    print(content)
