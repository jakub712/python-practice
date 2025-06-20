#You have 6 numbers: 42, 13, 90, 33, 5, 72.
#Check if all of them are even numbers.
#Use a Boolean flag to track this.

nums = (42, 13, 90, 33, 5, 72)

found = False

for i in nums: 
    if i % 7 == 0:
        found = True