s = "dictionary"
# Step-by-step:
# 1. Use a dictionary to count how many times each vowel appears.
# 2. Use `.get()` to update counts.
# 3. Only track vowels: a, e, i, o, u.
# Expected: {'i': 2, 'o': 1, 'a': 1}

result = {}
x = "a", "e", "i", "o", "u"

for letter in s:
    result[letter] = result.get(letter, 0) +1

new = {}
for letter in s:
    if letter in x:
        new[letter] = new.get(letter, 0) +1

print(new)