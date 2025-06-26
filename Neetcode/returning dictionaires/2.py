# ⏱ 5 min  
# 22. Build a dictionary from two lists using range and a loop  

# Input:  
keys = ['a', 'b']  
values = [3, 4]  
# Output:  
#{'a': 3, 'b': 4}

result = {}
for i in range(len(keys)):
    result[keys[i]] = values[i]

print(result)  # {'a': 1, 'b': 2}

