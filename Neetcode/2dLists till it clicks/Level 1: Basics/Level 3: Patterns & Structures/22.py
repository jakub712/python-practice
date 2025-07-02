nums = [100, 4, 200, 1, 3, 2]
target = 202
my_dict = {}

for index, num in enumerate(nums):
    complement = target - num
    if complement in my_dict:
        print([my_dict[complement], index])
        break
    my_dict[num] = index