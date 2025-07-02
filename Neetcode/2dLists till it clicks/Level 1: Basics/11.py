# Create a 4x3 grid where each value is row - col
# Output: [[0, -1, -2], [1, 0, -1], [2, 1, 0], [3, 2, 1]]

rows = 4
cols = 3
grid = []

for row in range(rows):
    new_row = []
    for col in range(cols):
        new_row.append (row -col)
    grid.append(new_row)
print(grid)