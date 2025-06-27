# Input:
nums = [5, 2, 9, 4]

# Goal:
# Print the difference between each pair: nums[i+1] - nums[i]
# Output: -3, 7, -5
max_diff = float('-inf')

for i in range(len(nums)-1):
    diff = nums[i +1] - nums[i]
print(diff)