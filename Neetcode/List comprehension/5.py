numbers = [1, 2, 3, 4, 5, 6]
# Your task: Use list comprehension to get only the odd numbers from the list.

odds= [nums for nums in numbers if nums % 2 != 0]
print(odds) 