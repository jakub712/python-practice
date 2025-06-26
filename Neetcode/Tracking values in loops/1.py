# ⏱ 5 min  
# 29. Count how many times 7 appears in a list  

# Input:  
nums = [7, 1, 7, 3, 7]  
# Output:  
3
count = 0 
for num in nums:
    if num == 7:
        count +=1 
        print(count)