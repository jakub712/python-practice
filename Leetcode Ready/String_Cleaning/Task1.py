text = "Welcome to 2025!"
cleaned = ""

for char in text:
    if char.isalpha():
        cleaned += char.lower()


print(cleaned)