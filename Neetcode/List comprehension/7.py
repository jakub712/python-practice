words = ["apple", "banana", "apricot", "cherry"]
# Your task: Use list comprehension to extract strings that start with the letter "a".

starts = {word for word in words if word[0] == 'a'}

print(starts)