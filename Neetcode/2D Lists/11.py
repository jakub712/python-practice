grid = [
    [1, 2],
    [3, 4],
    [5, 6]
]
# Your task: Flatten the 2D list into a 1D list using list comprehension.
x = [num for row in grid for num in row]

print(x)