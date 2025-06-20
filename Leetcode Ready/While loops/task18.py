#Task 3 – Palindrome with Ignored Punctuation

#Instructions:
#Check if a string is a palindrome while:

#    Ignoring spaces

#    Ignoring punctuation (like .,:!?)

#    Ignoring case

sentance = "A man, a plan, a canal: Panama" 
cleaned =""

for char in sentance:
    if char.isalnum():         # Keep only letters/numbers
        cleaned += char.lower()

left = 0 
right = len(cleaned) -1

while left < right:
    if cleaned[left]!=cleaned[right]:
        print(False)
        break
    left+= 1
    right -=1
else:
    print(True)