s = "ab3d5f2a1b3"
# Step-by-step:
# 1. Loop through the string.
# 2. Use `.get()` to count how many times each digit appears (ignore letters).
# Expected: {'3': 2, '5': 1, '2': 1, '1': 1}
result = {}

for letter in s:
    result[letter] = result.get(letter, 0)+1

new = {}

for letter in s:
    if letter.isnumeric():
        new[letter] = new.get(letter, 0) +1

print(new)