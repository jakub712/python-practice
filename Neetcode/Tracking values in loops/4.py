# ⏱ 5 min  
# 32. Count how many values are greater than 10  

# Input:  
nums = [5, 15, 20, 8]  
# Output:  
#2
counter = 0

for num in nums:
    if num > 10:
        counter += 1
print(counter)