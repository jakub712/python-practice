#Task 5 – “Selective Twin Hunter”
#Input:word = "xxabbyccddzzppxqrrqpp"
#Rules:You are hunting repeating pairs BUT:
#Only print the first character of a repeating pair
#BUT ONLY if:
#It’s not x, z, or q
#AND it’s surrounded by different letters (if possible)

word = "xxabbyccddzzppxqrrqpp"
i = 0

while i < len(word):
    if i > 0 and i < len(word) -1 and word[i] == word[i + 1] and word [i]not in "xzq" and word[i -1] != word [i + 1]:
        print(word[i])
        i += 1
    else:
        i += 1