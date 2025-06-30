words = ["apple", "banana", "cherry", "date", "grape"]
# Your task: Use list comprehension to extract strings with more than 5 characters.
who = [letter for letter in words if len(letter) > 5]
print(who)