s = "swiss"
# Step-by-step:
# 1. Count frequencies of each character in s.

result = {}
for word in s:
    result[word] = result.get(word, 0 ) +1
print(result)