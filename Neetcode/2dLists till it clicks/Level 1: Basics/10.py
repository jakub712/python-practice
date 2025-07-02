# Create a 2x4 grid where every cell is the sum of row and col indices, doubled.
# Output: [[0, 2, 4, 6], [2, 4, 6, 8]]
rows = 2
cols = 4
grids = []

for row in range(rows):
    new_row = []
    for col in range (cols):
        new_row.append((row + col) * 2)
    grids.append(new_row)

print(grids)