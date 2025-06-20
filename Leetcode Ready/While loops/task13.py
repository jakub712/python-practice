#Task 3: Detect the Letter Between Twins
# Input:word = "azbbazy"

#Goal:Print any character that has the same letter on both sides of it.
#So "aza" → print z,
#"bbb" → print b

word = "abcbcbacbb"
i = 0

while i < len(word):
    if i > 0 and i < len(word)-1 and word[i -1] == word[i +1]:
        print(word[i])
        i += 1
    else:
        i += 1