# Task 8: Skip Mirror Twins

#Instruction:

#Loop through the word "abccbazzyyzz"

#    If a character has the same letter on both sides of it, skip it.

#    Print only the characters that do not have matching neighbors.

#    Use a while loop.

#    Manually control i.

#    At the end, print "done!".

word = "abccbazzyyzz"
i = 0 

while i < len(word):
    if i < len(word) - 1 and word[i] == word[i + 1]:
        i += 2  # Skip the mirror twin
    else:
        print(word[i])
        i += 1
