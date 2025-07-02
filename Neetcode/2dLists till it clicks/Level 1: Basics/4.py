grid = [
    [5, 6, 7],
    [8, 9, 10]
]
# Loop through all elements and print them on one line.
# Output: 5 6 7 8 9 10

for row in grid:
    for num in row: 
        print(num,end = ' ')
