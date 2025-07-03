my_dict = {
    'car': 'Bentley',
    'job': 'software_dev',
    'income': '100k',
    'pets': 'none',
    'age': '25',
}
#Now create a new dict with only the keys that have values longer than 5 characters.
new_dict = {}

for key,value in my_dict.items():
    if len(value) > 5:
        new_dict[key] = value

print(new_dict)