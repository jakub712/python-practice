# 1. Count how many even numbers are in a list:
nums = [1, 4, 6, 9, 12, 15, 18]
counter = 0
for i in nums:
    if i % 2 == 0:
        counter += 1
       
print (counter)