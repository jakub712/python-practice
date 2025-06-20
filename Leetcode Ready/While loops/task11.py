# Input: word = "applebeetree"

# Print only the *first* letter of each double (repeating) pair.
# So output: p, e, e



word = "applebeetree"
i = 0

while i < len(word):
    if i > 0 and i < len(word) - 1 and word[i] == word[i + 1]:
        print(word[i])
        i += 2
    else:
        i += 1