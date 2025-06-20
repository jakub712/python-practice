#Task 5: Age Gate

#Ask for an age. If under 13, print "Child".
#13–17, print "Teen".
#18+, print "Adult".

age = int(input("How old are you?"))

if age < 13:
    print ("Your a child")
elif age > 13 and age < 1:
    print("You are a teen")
else:
    print("You are an Adult")