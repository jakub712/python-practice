numbers = [1, 2, 3, 4, 5, 6]
# Your task: Use list comprehension to double even numbers and triple odd numbers.

y = [nums * 2 if nums % 2 ==0 else nums * 3 for nums in numbers]

print(y)