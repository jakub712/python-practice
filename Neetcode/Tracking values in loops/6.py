# ⏱ 6 min  
# 38. Use continue to skip odd numbers and collect evens  

# Input:  
nums = [1, 2, 3, 4, 5]  
# Output:  
#[2, 4]
output = [0,0]
for num in nums:
    if num % 2 == 0:
        output = [num, num]
        print(num)