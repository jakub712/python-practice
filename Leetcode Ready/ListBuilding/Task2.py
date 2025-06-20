# build a lis of words that are 3 letters or less
list =[]
words = ["hi", "programming", "cat", "government", "dog"]

for i in words: 
    if len(i) > 3:
        continue
    else:
        list.append(i)

print(list)