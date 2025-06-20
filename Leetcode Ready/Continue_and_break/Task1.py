#TASK 1:Skip Vowel

word = "Python is fun"
vowel = "A", "E", "I", "O", "U", "a", "e", "i", "o", "u"

for i in word:
    if i in vowel:
        continue
    else:
        print(i)