s = "aabbcabc"
# Step-by-step:
# 1. Use a hashmap to tally each char.
# 2. Traverse s from start.
# 3. Return the first char appearing only once.
result = {}

for letter in s:
    result[letter] = result.get(letter, 0) +1


for letter in s:
    if result [letter] == 1:
        print(letter)
        break
else:
    print(None)
        



