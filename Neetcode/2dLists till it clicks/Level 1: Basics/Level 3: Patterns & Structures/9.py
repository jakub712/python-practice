s = "leetcode"
# Step-by-step:
# 1. Build a dict of character → count.
# 2. Iterate over s.
# 3. Return the first char with count == 1.

result = {}

for letter in s:
    result[letter] = result.get(letter, 0) +1

for letter in s:
    if result [letter] == 1:
        print(letter)
        break
