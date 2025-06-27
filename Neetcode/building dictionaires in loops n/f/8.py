# Given:
names = ['Alice', 'Bob', 'Charlie']
scores = [90, 85, 92]

# Goal:
# Create a dictionary where each name is a key and the corresponding score is its value.
# Expected:
# {'Alice': 90, 'Bob': 85, 'Charlie': 92}

result = {}

for i in range(len(names)):
    result [names[i]] = scores[i]
print(result)