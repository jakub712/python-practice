#Task 5: Double Letters Only

#Loop through the word "bookkeeper" and print only the letters that appear twice in a row (like oo, kk, ee).

word = "bookkeeper"
i = 0

while i < len(word) - 1:
    if word[i] == word[i+1]:
        print(word[i])
        i += 2
    else:
        i += 1
