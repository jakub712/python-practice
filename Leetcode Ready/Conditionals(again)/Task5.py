#Task 5:

#Title: “Almost a Match”

#Instructions:
#You have two numbers and one letter.

#    If both numbers are divisible by 5 and the letter is a consonant, print "Solid match".

#    If only one number is divisible by 5 or the letter is a consonant, print "Partial match".

#    Otherwise, print "Mismatch".

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
letter = input("Enter a letter: ")

if a % 5 == 0 and b % 5 == 0 and letter not in "aioeu":
    print("Solid Match!")
elif a % 5 == 0 and b % 5 != 0 and letter not in "aioeu":
    print("Partial Match")
else:
    print("Mismatch")