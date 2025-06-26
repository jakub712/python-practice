# Find the index of the first occurrence of the word "dog"
animals = ['cat', 'dog', 'fish', 'dog', 'bird']
for i, val in enumerate(animals):
    if val == "dog":
        print (i)
        break
