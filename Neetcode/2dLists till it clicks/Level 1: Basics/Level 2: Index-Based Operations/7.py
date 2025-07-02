# Step-by-step:
# 1. Create a 2x3 grid of 2s.
# 2. Use indexing (not a loop) to access the top-right cell.
# 3. Set it to 8.
rows = 2
cols = 3
grid = []

for row in range(rows):
    new_grid = []
    for col in range(cols):
        new_grid.append(2)
    grid.append(new_grid)

grid[0][2] = 8

print(grid)