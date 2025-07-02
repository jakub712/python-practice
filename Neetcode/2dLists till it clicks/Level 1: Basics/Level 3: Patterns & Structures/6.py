s = "121212003300"

i = {}

for word in s:
    i[word] = i.get(word, 0) +1

print(i)
