### ✅ Q3 — Loop + Condition

#Print all even numbers using loops.

# Step-by-step:
# 1. Use nested loops to go through all rows and columns.
# 2. Use an if condition to check if the number is even.
# 3. Print it inline (use print(num, end=' '))

grid = [
    [4, 7, 2],
    [9, 10, 13],
    [8, 1, 6]
]

for row in grid:
    for num in row: 
        if num % 2 != 0:
            print(num, end=' ')