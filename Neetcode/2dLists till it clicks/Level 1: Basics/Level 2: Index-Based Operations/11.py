# Step-by-step:
# 1. Make a 4x2 grid of large numbers.
# 2. Loop over each number.
# 3. Print it only if it's > 100.

grid = [
    [55, 200],
    [150, 99],
    [123, 76],
    [101, 300]
]

for row in grid:
    for num in row:
        if num > 100:
            print(num, end= ' ')