#Task 4: Print Only Vowels

#Loop through the string "grapefruit"

#    Use a while loop

#    Print only vowels

#    Ignore consonants

#    Print "done!" at the end

word="grapefruit"
i = 0

while i < len(word):
    character = word[i]
    if character in "aeiou":
        print (character)
        i += 1
    else:
        i += 1

print("done!")