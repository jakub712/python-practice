nums = [1, 2, 3, 4, 3]
target = 6
my_dict = {}

for index, num in enumerate(nums):
    complement = target - num
    if complement in my_dict:
        print([my_dict[complement], index])
        break
    my_dict[num] = index