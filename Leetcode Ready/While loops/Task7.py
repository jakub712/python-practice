#Task 7 – Remove characters next to duplicates

#Goal:
#Use a while loop to loop through the word:

#word = "abbccdeeffggh"

#If any character has the same letter next to it (left or right), remove both the character and its neighbor.

word = "abbccdeeffggh"
i = 0 

while i < len(word): 
    if i > 0 and i < len(word) -1 and word[i] == word [i +1]:
        i += 2
    else:
        print(word[i]) #this was the only error where i had to check old code for 
        i +=1

# Did it all alone 