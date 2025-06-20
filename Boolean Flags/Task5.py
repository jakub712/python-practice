#You have 8 numbers: 19, 28, 37, 46, 55, 64, 73, 82.
#Check if all of them are greater than 10 and less than 100.
#Use a Boolean flag to track this.

nums = (19, 28, 37, 46, 55, 64, 73, 82)
more_less = False

for i in nums:
    if i > 10 and i < 100:
        more_less = True