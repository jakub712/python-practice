#Task 7:

#Title: “The Sacred Pyramid”

#Instructions:
#You are given three numbers: a, b, c
#You must determine the order and divisibility to enter the "sacred pyramid"...

#Rules:

#    Print "Entered" if:

#        a < b < c and

#        all three numbers are even

#    Print "Wait" if:

#        a < b < c but only two of them are even

#    Print "Denied" if:

#        The order is not strictly increasing

#        Or less than two numbers are even

a = int(input("First number: "))
b = int(input("Second number: "))
c = int(input("Third number: "))
if a < b < c and a % 2 ==0 and b % 2 ==0 and c % 2 ==0:
    print("Entered")
elif a < b < c and a % 2 ==0 and b % 2 ==0 and c % 2 !=0:
    print("Wait")
elif a < b < c and a % 2 ==0 and b % 2 !=0 and c % 2 ==0:
    print("wait")
elif a < b < c and a % 2 !=0 and b % 2 ==0 and c % 2 ==0:
    print("Wait")
else:
    ("Denied")
#after talking to my ai for a while i relised the complex conditionalls that hurt my brain only show up in loops i started this segmant...
# to help my while loops but it was unecassery slightly anoyed atm....
