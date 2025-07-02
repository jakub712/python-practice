# Create a 4x2 grid where each element is the sum of its row and column index.

# Expected Output:
# [
#   [0, 1],
#   [1, 2],
#   [2, 3],
#   [3, 4]
# ]

rows = 4
cols = 2
grid = []

for row in range(rows):
    new_row = []
    for col in range(cols):
        new_row.append(row + col)
    grid.append(new_row)

print(grid)