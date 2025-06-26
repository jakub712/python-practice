# Input:
word = "hello"
# Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}
counts = {} 

for letter in word:
    if letter not in counts:
        counts[letter] = 1
    else:
        counts[letter] += 1

print(counts)