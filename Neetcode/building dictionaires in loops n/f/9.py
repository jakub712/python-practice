# Given:
letters = ['a', 'b', 'a', 'c', 'b', 'a']

# Goal:
# Build a dictionary that counts how many times each letter appears.

# Expected:
# {'a': 3, 'b': 2, 'c': 1}

result = {}

for letter in letters:
    if letter in result:
        result[letter] +=1
    else:
        result[letter] =1
print(result)
