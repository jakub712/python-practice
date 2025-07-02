s = "aabbcddex"
# Step-by-step:
# 1. Use a dictionary to count frequencies of each character.
# 2. Loop through the string again.
# 3. Return the first character with a count of 1.

result = {}
for word in s:
    result[word] = result.get(word, 0 ) +1

print(result)