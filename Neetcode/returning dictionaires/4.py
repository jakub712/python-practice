# ⏱ 6 min  
# 24. Write a function that returns a dictionary built from two lists  

# Input:  
keys = ['id', 'name']  
values = [123, 'Alice']  
# Output:  
#{'id': 123, 'name': 'Alice'}
result = {}
for i in range(len(keys)):
    result[keys[i]] = values[i]

print(result)  