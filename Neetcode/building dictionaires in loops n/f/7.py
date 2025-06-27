# Given:
chars = ['h', 'e', 'l', 'l', 'o']

# Goal:
# Count how many times each letter appears.
# Expected:
# {'h': 1, 'e': 1, 'l': 2, 'o': 1}

result = {}
for letter in chars:
    if letter in result:
        result[letter] += 1
    else:
        result[letter] = 1
print(result)