# Input:
nums = [2, 3, 4]
# Output: {2: 4, 3: 9, 4: 16}

values = [[nums[0] * nums[0]], [nums[1] * nums[1]],[nums[2] * nums[2]]]

result = {}
for i in range(len(nums)):
    result[nums[i]] = values[i]

print(result)