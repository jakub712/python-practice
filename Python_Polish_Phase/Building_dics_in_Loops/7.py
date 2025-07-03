info = {
    "name": "Jakub",
    "hobby": "card magic",
    "goal": "backend dev"
}

# 🔁 Build new_dict where values are replaced with their string lengths.
my_dict = {}
for key,value in info.items():
    my_dict[key] = len(value)

print(my_dict)