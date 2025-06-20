word = "Eva, can I see bees in a cave?" #combining cleaning and skipping one bad word two pointers, can't belive i did it.
cleaned = ""

for char in word:
    if char.isalpha():
        cleaned += char.lower()

l = 0 
r = len(cleaned) -1

while l < r:
    if cleaned [l] != cleaned [r]:
        a, b = l +1, r
        while a < b and word[a] == word [b]:
            print(True)
            break


        a,b = l, r -1
        while l < r and cleaned[a] == cleaned[b]:
            print (True)
        else:
            print(False)
        break

    else:
        l += 1
        r -= 1
else: 
    print(True)