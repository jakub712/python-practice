# ⏱ 5 min  
# 21. Create a dictionary from two lists using a loop  

# Input:  
keys = ['a', 'b']
values = [1, 2]

result = {}
for i in range(len(keys)):
    result[keys[i]] = values[i]

print(result)  # {'a': 1, 'b': 2}
