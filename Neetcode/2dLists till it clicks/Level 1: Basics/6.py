grid = [
    [0, 9],
    [8, 7],
    [6, 5],
    [4, 3]
]
# Output: 0 9 8 7 6 5 4 3

for row in grid:
    for num in row:
        print(num,end=' ')