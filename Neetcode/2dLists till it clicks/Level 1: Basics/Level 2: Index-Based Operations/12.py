# Step-by-step:
# 1. Make a 3x3 grid containing some 0s.
# 2. Loop through rows and columns.
# 3. Print each 0 on the same line.
grid = [
    [0, 1, 2],
    [3, 0, 4],
    [5, 6, 0]
]

for row in grid:
    for num in row:
        if num == 0:
            print (num, end='')