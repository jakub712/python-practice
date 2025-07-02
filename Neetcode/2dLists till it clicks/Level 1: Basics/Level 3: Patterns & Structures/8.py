s = "swiss"
# Step-by-step:
# 1. Count frequencies of each character in s.
# 2. Loop through s in order.
# 3. Return the first character whose count is 1.

result = {}

for word in s:
    result[word] = result.get(word, 0) + 1

for word in s:
    if result[word] == 1:
        print(word)
        break