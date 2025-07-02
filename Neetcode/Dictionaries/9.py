# Q9. Given a dictionary {"a": 1, "b": 2}, double all values.

y = {"a": 1, "b": 2}
n = {}
for key, value in y.items():
    k = {key : value *2}

    print(k)
