# Q12. Count letter frequency in the word "hello" using .get() instead of if/else.
words = "hello"
result = {}

for word in words:
    result[word] = result.get(word, 0) + 1

print(result)