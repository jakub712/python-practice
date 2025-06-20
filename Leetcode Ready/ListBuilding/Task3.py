#Build a list of characters from the string that are didgets.
text ="ab5c9d1e"
list = []

for i in text: 
    if i.isalpha():
        continue
    else:
        list.append(i)

    print(i)