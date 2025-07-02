# Step-by-step:
# 1. Create a 3x3 grid of 5s.
# 2. Use a loop to access each column of the last row (row index 2).
# 3. Set each value to 0.

rows = 3
cols = 3
grid = []

for row in range(rows):
    new_grid = []
    for col in range(cols):
        new_grid.append(5)
    grid.append(new_grid)

for col in range(cols):
    grid[2][col] = 0

print(grid)
