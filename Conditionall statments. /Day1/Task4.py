#Task 4: Grade Checker

#Ask for a number (0–100). Print:

 #   "A" if 90+

  #  "B" if 80–89

   # "C" if 70–79

    #"D" if 60–69

    #"F" if below 60

marks = int(input("How many marks did you get?"))
if marks >= 90:
    print("You got an A")
elif marks > 80 and marks < 89:
    print("Your grade is a B")
elif marks > 70 and marks < 79:
    print("Your grade is a C")
elif marks > 60 and marks < 69:
    print("Your grade is a D")
else:
    print("Your grade is a F")