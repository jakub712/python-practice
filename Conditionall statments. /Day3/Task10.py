#Create a loop that keeps asking the user for a number. If the number is even, print "Even" and stop. If odd, keep asking.
#Use while and conditionals.


while True:
    num = int(input("Give me a number: "))
    if num % 2 == 0: 
        print ("even")
        break
    else:
        print("The number is odd try again.")