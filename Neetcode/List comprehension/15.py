words = ["apple", "banana", "cherry", "date"]
# Your task: Use list comprehension to remove strings containing the letter "a".
cleaned_words = [''.join([letter for letter in word if letter != 'a']) for word in words]
print(cleaned_words)

#