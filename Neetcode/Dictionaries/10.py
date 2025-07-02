# Q10. Print a list of all keys whose value is greater than 10.
y =  {"a": 5, "b": 15, "c": 20}

k = {}

for key, value in y.items():
    if value > 10:
        k = {key}

        print(k)
