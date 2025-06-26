# ⏱ 6 min  
# 39. Track running sum until it exceeds 100 and return index  

# Input:  
nums = [10]*15  
# Output:  
#10
total = 0

for i in range(len(nums)):
    total += nums[i]
    if total > 100:
        print(i)
        break

        