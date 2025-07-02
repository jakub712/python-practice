# Step-by-step:
# 1. Make a 2x4 grid of mixed numbers.
# 2. Use nested loops to go through the grid.
# 3. Print only the odd numbers inline.

grid = [
    [4, 7, 10, 13],
    [2, 5, 8, 11]
]

for row in grid:
    for num in row:
        if num % 2 != 0:
            print(num, end=' ')