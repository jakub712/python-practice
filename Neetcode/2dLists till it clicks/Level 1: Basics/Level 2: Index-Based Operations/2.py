# Step-by-step:
# 1. Create a 2x4 grid of 1s.
# 2. Use a loop to access each column of row index 1.
# 3. Set each value to 0.

rows = 2
cols = 4
grid = []

for row in range(rows):
    new_grid = []
    for col in range(cols):
        new_grid.append(1)
    grid.append(new_grid)

for col in range(cols):
    grid[1][col] = 0

print(grid)