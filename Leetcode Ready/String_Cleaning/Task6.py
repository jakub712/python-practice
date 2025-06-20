text = "A man, a plan, a canal: Panama"
cleaned = ""

for char in text:
    if char.isalpha():
        cleaned += char.lower()

print(cleaned)

l = 0
r = len(cleaned) -1

while l <r:
    if cleaned[l] != cleaned [r]:
        print(False)
        break
    l += 1
    r -= 1
else:
    print(True)
