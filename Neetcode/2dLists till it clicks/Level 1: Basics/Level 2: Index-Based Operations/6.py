# Step-by-step:
# 1. Create a 5x5 grid of 1s.
# 2. Use a nested loop over all rows and columns.
# 3. If row == col, set the cell to 0.

rows = 5
cols = 5
grid = []

for row in range(rows):
    new_grid = []
    for col in range(cols):
        if row == col:
            new_grid.append(0)
        else:
            new_grid.append(1)
    grid.append(new_grid)


print(grid)