# Input:
nums = [10, 3, 8, 22]

# Goal:
# Print the largest adjacent difference using nums[i+1] - nums[i]
# Output: 14
max_diff = float('-inf')

for i in range(len(nums)-1):
    diff = nums[i +1] - nums[i]
    max_diff = max(max_diff,diff)

print(max_diff)