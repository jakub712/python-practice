# Q3. Count how many times each letter appears using .get()
word = "apple"
# Expected: {'a':1, 'p':2, 'l':1, 'e':1}
result = {}

for letter in word:
    result[letter] = result.get(letter,0) +1

print(result)