grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Your task: Create a new list that contains the maximum value of each row using list comprehension.
x = [ max(i) for i in grid]
print(x)