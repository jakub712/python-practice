#Title: "Even and Vowel"

#Instructions:
#You’re given a number and a letter.

#    If the number is even and the letter is a vowel, print "Perfect match".

#    If only one of the two conditions is true, print "Half match".

#    If neither is true, print "No match".
num = int(input("Pick a number: "))
letter = input("Pick a letter: ")

if num % 2 == 0 and letter in "aioeu":
    print("Perfect match!")
elif num % 2 ==0 and letter not in "aioeu":
    print("Half match")
elif num % 2 != 0 and letter in "aioeu":
    print ("Half match")
else:
    print("No match")