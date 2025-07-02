# Create a 3x3 grid where each value is row * col
# Output: [[0, 0, 0], [0, 1, 2], [0, 2, 4]]
rows = 3
cols = 3
grid = []

for row in range(rows):
    new_row = []
    for col in range(cols):
        new_row.append(row * col)
    grid.append(new_row)

print(grid)