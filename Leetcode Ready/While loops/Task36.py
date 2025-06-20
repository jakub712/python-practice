word = "No lemon, no melon"
cleaned = ""

for char in word:
    if char.isalpha():
        cleaned += char.lower ()

l = 0 
r = len(cleaned) -1

while l < r:
    if cleaned [l] != cleaned[r]:
        print(False)
        break
    else:
        l += 1
        r -= 1
print (True)