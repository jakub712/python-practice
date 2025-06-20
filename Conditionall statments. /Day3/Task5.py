#Loop through a string and print only the vowels.
#Use for and if char in "aeiou".
vowel = ("A", "E", "I", "O", "U", "a", "e", "i", "o", "u")
word = input("Write me a word: ")
found_vowel = False

for i in word:
    if i in vowel:
        print(i)
        found_vowel = True

if not found_vowel:
    print("There are no vowels")