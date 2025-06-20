#You have 5 numbers: 589, 25729, 24268, 1683, 1.
#Check if any of them are divisible by 7.
#Use a Boolean flag to track this.
#spent half an hour on this cant find anything on boolean flags online!

nums = (589, 25729, 24268, 1683, 1)

found = False

for num in nums:
    if num % 7 == 0:
        found = True