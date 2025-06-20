#Case-Insensitive + Space-Ignore Palindrome

#Instructions:Write a while loop that checks if a string is a palindrome while:
#Ignoring spaces
#Ignoring case differences

word = "Race Car"
word = word.lower()
word = word.replace(" ","")


left = 0
right = len(word) -1

while left < right:
    if word[left] != word[right]:
        print(False)
        break
    left += 1
    right -= 1
else:
    print(True)
        
