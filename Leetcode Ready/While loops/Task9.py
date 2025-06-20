#While Loop Task 9: Trapped Vowel Echo

#Prompt:
#You are given a string of letters. Print only the vowels that are trapped between two identical consonants.

#A vowel is “trapped” if:

#    The character before it and the character after it are the same consonant, and

#    The vowel itself is not duplicated.

word = "tobebobdut"
i = 0 
while i < len(word):
    if i > 0 and i < len(word) - 1 and word [i -1] == word [i +1]:
        print (word[i])
        i +=2 
    else: 
        i += 1