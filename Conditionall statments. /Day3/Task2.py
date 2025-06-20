#Print the numbers from 1 to 30. For multiples of 3, print "Fizz" instead of the number.
#Basic if inside loop.
for i in range (1, 31, 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
