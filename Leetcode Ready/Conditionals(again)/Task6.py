#Task 6:

#Title: “High Stakes”
#Instructions:
#You’re given three inputs:
#    A number x
#    A second number y
#    A letter

#Print "Jackpot" only if all three of the following are true:
#    x is greater than 100
#    y is a multiple of 7
#    The letter is a vowel
#If two out of three are true, print "Close"
#If only one is true, print "Try again"
#If none are true, print "No luck"

x = int(input("Enter a number: "))
y = int(input("Enter another number: "))
letter = input("Enter a letter: ")

if x > 100 and y % 7 == 0 and letter in "aeiou":
    print("Jackpot")
elif x <  100 and y % 7 != 0 and letter not in "aeiou":
    print("No luck")
elif x < 100 and y % 7 ==0 and letter in "aeiou":
    print("Try again")
elif x > 100 and y % 7 !=0 and letter in "aeiou":
    print("Try again")
elif x > 100 and y % 7 ==0 and letter not in "aeiou":
    print("Try again")
else:
    pass