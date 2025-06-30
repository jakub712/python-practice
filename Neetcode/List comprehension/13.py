numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Your task: Use list comprehension to find numbers that are divisible by 3.
three = [ num for num in numbers if num % 3 == 0]

print(three)