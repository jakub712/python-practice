# build the squares of even numbers only
# output -> [4, 16, 36]
nums = [2, 3, 4, 5, 6]
list = []

for i in nums:
    if i % 2 ==0:
        list.append (i*i)
    else:
        continue

print(list)