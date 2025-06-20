word =  " 123abc DEF!! "
cleaned = ""

for char in word:
    if char.isalpha():
        cleaned += char.lower()

print(cleaned)