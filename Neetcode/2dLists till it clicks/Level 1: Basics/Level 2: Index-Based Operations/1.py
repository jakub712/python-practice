# Step-by-step:
# 1. Create a 3x3 grid of zeroes.
# 2. Loop through rows and columns.
# 3. If it's the center cell, set it to 1.

cols = 3
rows = 3
grid = []

for row in range(rows):
    new_grid = []
    for col in range(cols):
        new_grid.append(0)
    grid.append(new_grid)

grid[1][1] = 1
print(grid)