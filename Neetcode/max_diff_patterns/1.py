# ⏱ 3 min
# 1. Find the largest difference between adjacent numbers

nums = [5, 9, 3, 14]
# Output: 11
max_diff= float('-inf')

for i in range (len(nums)-1):
    diff = nums[i+1] - nums[i]
    max_diff = max(max_diff, diff)
print(max_diff)