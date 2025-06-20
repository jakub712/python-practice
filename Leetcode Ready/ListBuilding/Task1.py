# get each odd number times it by three add it in a new list.
nums = [1, 4, 7, 10, 13]
odds = []

for i in nums:
    if i % 2 != 0:
        i *= 3
        odds.append(i)

print(odds)