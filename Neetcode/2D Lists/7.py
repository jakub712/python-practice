grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Your task: Create a new list containing the maximum value of each row.

x = [max(i) for i in grid]
print(x)