#Vowel Stripper, you are given a string create a new string that incldes only every second character excluding vowels
#example: "Mastery takes time" -> "Msytkstm"

word = "Mitchal Edwards"
word = word[:: 2]
vowels = "A", "E", "I", "O", "U", "a", "e", "i", "o", "u"
new_word = ""

for char in word:
    if char not in vowels:
        new_word += char

print(new_word)
