# Step-by-step:
# 1. Create a 3x3 grid of mixed numbers.
# 2. Use nested loops to go through the grid.
# 3. Print only the numbers greater than 50 inline.
# (use print(num, end=' '))

grid = [
    [12, 53, 7],
    [66, 42, 80],
    [49, 91, 30]
]


for row in grid:
    for num in row:
        if num > 50:
            print(num, end= ' ')