# Step-by-step:
# 1. Create a 3x3 grid of integers.
# 2. Use nested loops to access every number.
# 3. If it's divisible by 3, print it inline.
# (use print(num, end=' '))

grid = [
    [3, 5, 6],
    [7, 9, 12],
    [15, 18, 20]
]

for rows in grid:
    for num in rows:
        if num % 3 == 0:
            print(num, end=' ')