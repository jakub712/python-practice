sentence = "i love love python python python"
# Step-by-step:
# 1. Split the sentence into words.
# 2. Use a dictionary with `.get()` to count how many times each word appears.
# Expected: {'i': 1, 'love': 2, 'python': 3}
x = sentence.split()
result = {}

for letter in x:
    result[letter] = result.get(letter, 0) +1

print(result)