# Input:
keys = ['a', 'b']
values = [1, 2]
# Output: {'a': 1, 'b': 2}
result = {}
for i in range(len(keys)):
    result[keys[i]] = values[i]

print(result)