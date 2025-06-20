#Task 1 – First and Last Letter Swap
#You are given a string like "python".
#Swap the first and last characters using indexing and slicing only.
#Print the result.

word = "python"

new_word = word[-1] + word[1:-1] + word[0]

print(new_word)