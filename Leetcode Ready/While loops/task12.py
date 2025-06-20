# Input: word = "mississippi"

# Print all characters, skipping over any pair that repeats (like ss, pp).

# Output should be: m, i, i, i

word = "mississippi" 
i = 0 

while i < len(word):
    if i > 0 and i < len(word) -1 and word[i] == word[i + 1]:
        i += 2
    else:
        print(word[i])
        i += 1
