word =  "@Hello##$$World!!"
cleaned =""

for char in word:
    if char.isalpha():
        cleaned += char.lower()

print(cleaned)