word ="Coding is 100% fun :) "
cleaned = ""

for char in word:
    if char.isalpha():
        cleaned += char.lower()

print(cleaned)