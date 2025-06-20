#Two-Pointer Challenge:

#Question:
#Write a program that checks if a string can become a palindrome after removing at most one character.
#Example inputs:

#    "abca" → True (remove b)

#    "racecar" → True

#    "abcdef" → False

#Make sure to:

#    Use two pointers

#    Try both skipping the left or right character when there's a mismatch

#Let me know once you're done or if you want a hint.

word = "abca"
l = 0
r = len(word) -1

while l < r:
    if word [l] != word[r]:
        a,b = l +1, r
        while a < b and word[a] == word[b]:
            a += 1
            b -=1
        if a >= b:
            print (True)
            break

        a, b = l, r -1
        while a < b and word [a] == word[b]:
            a +=1
            b -=1
        if a >= b:
            print (True)
        else:
            print(False)
        break
    else:
        l +=1
        r -=1
else:
    print(True)