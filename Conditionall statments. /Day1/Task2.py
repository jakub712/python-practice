# Task 2: Positive, Negative, or Zero
#Ask for a number. Print "Positive", "Negative", or "Zero" depending on the input.
number = int(input ("Give me a number posotive or negative, even zero!"))
if number < 0:
    print ("Negative")
elif number == 0:
    print("Zero")
else:
    print("Positive")
