numbers = [1, 2, 3, 4, 5]
# Your task: Use list comprehension to create a list of tuples (number, square).
lists = [ (num , num *num) for num in numbers]

print(lists)