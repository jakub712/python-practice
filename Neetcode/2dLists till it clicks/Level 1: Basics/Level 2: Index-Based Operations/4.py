# Step-by-step:
# 1. Create a 4x2 grid of 9s.
# 2. Use a loop to access each row.
# 3. Set the first column (col index 0) to 1.

rows = 4
cols = 2
grid = []

for row in range(rows):
    new_grid = []
    for col in range(cols):
        new_grid.append(9)
    grid.append(new_grid)

for row in range(rows):
    grid[row][0] = 1
print(grid)