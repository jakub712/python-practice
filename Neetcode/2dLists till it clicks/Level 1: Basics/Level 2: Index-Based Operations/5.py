# Step-by-step:
# 1. Create a 3x3 grid of 0s.
# 2. Use a loop over cols of row index 2.
# 3. Set the middle column (col index 1) to 99.

rows = 3
cols = 3
grid = []

for row in range(rows):
    new_grid = []
    for col in range(cols):
        new_grid.append(0)
    grid.append(new_grid)

for col in range(cols):
    grid[2][1] = 99

print(grid)