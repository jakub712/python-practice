def get_sorted_words(words: list[str]) -> list[str]:
    """Sort a list of words alphabetically A → Z"""
    words.sort()
    return words

def get_length_words(words: list[str]) -> list[str]:
    words.sort(key = lambda word: len(word))
    return(words)

def get_nums_vowels(word: list[str]) -> int:
    vowels = "aeiou"
    counter = 0 
    for i in word: 
        if i in vowels: 
            counter +=1
    return counter

def sort_num_vowels(words: list[str]) -> list [str]:
    words.sort(key = get_nums_vowels)
    return words

sen = input("Enter a sentence: ")
cleaned = ""
for char in sen:
    if char.isalpha() or char.isspace():
        cleaned+=char 

words = cleaned.split()

choice = input(""" 
How would you like to sort the words?
1 - Alphabetically (A -> Z)
2 - By word length
3 - By number of vowels
4 - Exit
""")

if choice == "1": 
    sorted_words = get_sorted_words(words)
    print(sorted_words)

if choice == "2":
    length_words = get_length_words(words)
    print(length_words) 

if choice == "3":
    num_vowels = sort_num_vowels(words)
    print(num_vowels)

if choice == "4":
    print("okay?\U0001F644")