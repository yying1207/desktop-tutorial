import json

json_data = '{"name": "john", "age": 30, "city": "New York"}'

# Parse JSON data to python
data = json.loads(json_data)

print(data)
print(data['name'])
print(data['age'])

data['country'] = 'CN'
data['age'] = 28
print(data)


# Parse python data to JSON
updated_json_data = json.dumps(data)
print(updated_json_data)


# Write the data to a JSON file named "output.json"
with open('output.json', 'w') as file:
    json.dump(data, file)


# Read the data from the JSON file "output.json"
with open("output.json", "r") as file:
    read_data = json.load(file)

print(read_data)