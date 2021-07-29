import json
with open('json_example.json', 'r') as file:
    data = json.load(file)
user = data['user']
print(user['name'])
for role in user['roles']:
    print(role)

user['location']['city'] = 'Dallas'
with open('json_example-edited.json', 'w') as file2:
    json.dump(data, file2, indent=4)
