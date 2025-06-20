# build a list that meets all these conditions,
#they are letters, not vowels, the index is even 
text = "The moon is 1/4 full"
list=[]
vowels = ("a", "e", "i", "o", "u")

for i in range(len(text)):
    char = text[i]
    if i % 2 == 0 and char.isalpha() and char not in vowels:
        print(char)