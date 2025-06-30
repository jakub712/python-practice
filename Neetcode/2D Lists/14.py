grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Your task: Use list comprehension to create a new list with all the even numbers from the grid.
x = [[i for i in row if i % 2 == 0] for row in grid]
print(x)

