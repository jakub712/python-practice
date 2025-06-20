#You have 4 numbers: 12, 25, 38, 47.
#Check if none of them are less than 10.
#Use a Boolean flag to track this.

nums = (12, 25, 38, 47)

less_than_ten = False

for i in nums:
    if i < 10:
        less_than_ten = True