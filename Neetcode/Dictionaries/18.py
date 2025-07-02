# Q6. Loop through this list of names and count how often each name appears.
names = ["Tom", "Bob", "Tom", "Alice", "Bob"]
# Use .get()
result = {}

for name in names:
    result[name] = result.get(name, 0) +1

print(result)