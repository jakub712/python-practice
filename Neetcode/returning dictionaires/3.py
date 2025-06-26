# ⏱ 5 min  
# 23. Add key-value pairs to an empty dictionary inside a for loop  

# Input:  
keys = ['x', 'y']  
values = [10, 20]  
# Output:  
#{'x': 10, 'y': 20}

result = {}
for i in range(len(keys)):
    result[keys[i]] = values[i]

print(result)  