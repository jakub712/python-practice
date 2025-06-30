grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Your task: Use list comprehension to flatten the grid into a 1D list.
flat = [num for row in grid for num in row]
print(flat)