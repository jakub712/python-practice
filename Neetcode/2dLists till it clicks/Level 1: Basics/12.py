# Create a 5x1 grid where each value is row + 5
# Output: [[5], [6], [7], [8], [9]]

rows = 5
cols = 1
grid = []

for row in range(rows):
    new_grid = []
    for col in range(cols):
        new_grid.append(row + 5)
    grid.append(new_grid)
print(grid)