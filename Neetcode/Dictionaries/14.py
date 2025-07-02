# Q2. Use .get() to return the value of "x" in this dict.
# If "x" doesn’t exist, return 0
d = {"x": 5, "y": 6}

if d.get("x") == None:
    print(0)
else:
    print (d.get('x'))