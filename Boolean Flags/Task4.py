#You have 7 numbers: 11, 22, 33, 44, 55, 66, 77.
#Check if at least one number is a multiple of both 11 and 3.
#Use a Boolean flag to track this.

nums = (11, 22, 33, 44, 55, 66, 77)
is_multiple = False

for i in nums:
    if i % 11 == 0 and i % 3 == 0:
        is_multiple = True