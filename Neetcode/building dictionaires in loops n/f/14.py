# Input: [('x', 1), ('x', 2), ('y', 3)]
# Output: {'x': [1, 2], 'y': [3]}

nums = [('x', 1), ('x', 2), ('y', 3)]
result = {}

for num in nums:
    if num in result:
        result [num] .append(result)
    else:
        result[num] = [result]