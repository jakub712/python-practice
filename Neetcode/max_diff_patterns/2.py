# ⏱ 3 min
# 2. Print the difference between each pair: nums[i+1] - nums[i]

nums = [7, 13, 4, 12]
# Output: 6, -9, 8
max_diff = float('-inf')

for i in range(len(nums)-1):
    diff = nums [i+1] - nums[i]
    print(diff)