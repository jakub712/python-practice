numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# Your task: Use list comprehension to square the even numbers.

squared = [num * num for num in numbers if num % 2 == 0] 

print(squared)