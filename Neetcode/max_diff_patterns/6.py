# Input:
nums = [30, 10, 15, 50]

# Goal:
# Track the largest **positive** adjacent difference only
# Ignore negative diffs
# Output: 35

max_diff = float('-inf')

for i in range(len(nums)-1):
    diff = nums[i +1] - nums[i]
    if diff > 0:
        max_diff = max(max_diff,diff)

print(max_diff)