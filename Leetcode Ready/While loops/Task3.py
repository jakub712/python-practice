#Task 3: Loop Every 2nd Letter

#Loop through the string "watermelon"

#    Print every second letter only

#    Use a while loop

#    Print "done!" when it's complete

word = "watermelon"
i = 0 

while i < len(word):
    character = word[i]
    print(character)
    i +=2
print("done!")