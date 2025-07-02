nums = [1, 2, 3, 4, 3]
target = 6
# Return a list of unique pairs that add to target. Each pair should only appear once.
my_dict = {}

for index, num in enumerate(nums):
    complement = target - num
    if complement in my_dict:
        print([my_dict[complement], index])
        break
    my_dict[num] = index

