# Create a 3x3 grid where values are row squared + col
# Output: [[0, 1, 2], [1, 2, 3], [4, 5, 6]]
rows = 3
cols = 3
grid = []

for row in range(rows):
    new_grid = []
    for col in range(cols):
        new_grid.append ((row * row)+ col)
    grid.append(new_grid)
print(grid)