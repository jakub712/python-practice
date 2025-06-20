#Task 3:

#You have two numbers, a and b. Print "match" if only one of them is divisible by 3 (not both!).

a = input("Pick a number! ")
b = input("Pick another number! ")

x = int(a)
y = int(b)

if x % 3 == 0 and y % 3 ==0:
    print(":(")
elif y % 3 ==0:
    print ("match")
else:
    print ("Match")