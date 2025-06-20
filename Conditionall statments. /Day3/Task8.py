#Ask the user to enter words until they enter a palindrome.
#Check if the word equals its reverse.
i = input ("give me a palindrome. ")

i = i.lower()

if i == i [::-1]:
    print(i, "is a palindrome")
else:
    print( i, "is not a palindrome")

