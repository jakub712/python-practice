# Given:
words = ['hi', 'hello', 'python']

# Goal:
# Build a dictionary where:
# - each word is the key
# - the value is the length of the word

# Expected:
# {'hi': 2, 'hello': 5, 'python': 6}

result = {}

for word in words:
    result[word] = len(word)

print(result)