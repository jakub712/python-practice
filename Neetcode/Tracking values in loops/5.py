# ⏱ 6 min  
# 33. Track and update max value in a loop  

# Input:  
nums = [1, 8, 3, 9]  
# Output:  
#9
max = 0 
for num in nums:
    if num > max:
        max = num
print(max)