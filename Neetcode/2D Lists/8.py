grid = [
    [1, 2],
    [3, 4],
    [5, 6]
]
# Your task: Create a new 2D list where each element is doubled.
x = [[i * 2 for i in row] for row in grid]
print(x)