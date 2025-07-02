# Q5. Given a list of numbers, count how often each appears using .get()
nums = [1, 2, 1, 3, 2, 1]
# Expected: {1: 3, 2: 2, 3: 1}
result = {}

for num in nums:
    result[num] = result.get(num, 0) +1

print(result)