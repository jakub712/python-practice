# Given:
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 92, 78]

# Goal:
# Build a dictionary where each name maps to their score.
# Expected:
# {'Alice': 85, 'Bob': 92, 'Charlie': 78}

result = {}
for i in range(len(names)):
    result[names[i]] = scores[i]
print(result)