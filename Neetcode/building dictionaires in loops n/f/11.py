input = ['pen', 'pencil', 'pen', 'eraser']
# Output: {'pen': 2, 'pencil': 1, 'eraser': 1}

result = {}

for i in input:
    if i in result:
        result[i] += 1
    else:
        result[i] = 1
print(result)