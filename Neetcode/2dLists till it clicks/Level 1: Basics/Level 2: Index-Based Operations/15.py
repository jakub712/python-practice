### ✅ Q5 — Modify by Condition

#Change values > 10 to 10 in-place.

#python
# Step-by-step:
# 1. Use `for i in range(len(grid))`, then `for j in range(len(grid[i]))`
# 2. If grid[i][j] > 10, set grid[i][j] = 10
# 3. Print grid after modification

grid = [
    [5, 12, 7],
    [15, 3, 10],
    [8, 25, 11]
]


for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] > 10:
            grid[i][j] = 10

print(grid)