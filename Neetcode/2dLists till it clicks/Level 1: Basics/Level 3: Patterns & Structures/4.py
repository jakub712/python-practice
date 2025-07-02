s = "mississippi"

result = {}

for word in s:
    result[word] = result.get(word, 0) +1

print(result)