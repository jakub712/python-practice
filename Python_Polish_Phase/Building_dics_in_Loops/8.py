users = {
    "john": "admin",
    "lucy": "user",
    "mark": "admin",
    "sara": "guest"
}
# Build a new dictionary where:
    #Only users with the role "admin" are included.
    #The usernames (keys) are converted to uppercase.
    #The values stay the same ("admin").
my_dict = {}
for key, value in users.items():
    if value == 'admin':
        my_dict[key.upper()] = value



print(my_dict)