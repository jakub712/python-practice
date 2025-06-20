# If a character has the same letter on both sides of it, it must be removed.

word = "abcbab"
i = 0

while i < len(word):
    if i > 0 and i < len(word) - 1 and word[i - 1] == word[i + 1]:
        # Middle character between two same characters → skip
        #only the single line above was changed. 
        i += 1
    else:
        print(word[i])
        i += 1
# chat gpt gave the answwer this stuff is confusing to me 