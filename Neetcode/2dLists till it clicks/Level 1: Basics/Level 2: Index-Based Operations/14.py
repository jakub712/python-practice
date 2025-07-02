### ✅ Q4 — Count with Condition

#Count how many times 0 appears.

#python
# Step-by-step:
# 1. Use nested loops to iterate over grid.
# 2. Add 1 to a counter every time you see a 0.
# 3. Print the counter.

grid = [
    [0, 5, 0],
    [3, 0, 2],
    [7, 8, 0]
]

counter = 0

for row in grid:
    for num in row:
        if num == 0:
            counter +=1 
        
print(counter)