# Q11. Reverse a dictionary so that values become keys and keys become values.
y = {"a": 1, "b": 2}


k = {}

for key, value in y.items():
    k[value] = key    

print(k)