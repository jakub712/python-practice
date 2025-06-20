#Loop through numbers 1 to 50. Print "Fizz" for multiples of 3, "Buzz" for 5, and "FizzBuzz" for both.
#Nested if-elif-else.

for i in range (1, 51, 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
