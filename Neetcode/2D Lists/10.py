# Your task: Use list comprehension to create a 2D list of size 3x3, where each number is the index of its row.
x = [[i for _ in range(3)] for i in range(3)]

print(x)