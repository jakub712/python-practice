word =  "They said, 'Go!' and left."
cleaned =""

for char in word:
    if char.isalpha():
        cleaned += char.lower()

print(cleaned)