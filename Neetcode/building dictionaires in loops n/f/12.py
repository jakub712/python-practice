# Input:
names = ['John', 'Jane']
scores = [90, 95]
# Output: {'John': 90, 'Jane': 95}
result = {}

for i in range(len(names)):
    result[names[i]] = scores[i]
print(result)

