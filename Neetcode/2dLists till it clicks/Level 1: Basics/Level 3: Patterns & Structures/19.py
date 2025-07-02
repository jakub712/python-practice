nums = [4, 3, 2, 7, 8, 2, 3, 1]
target = 9
my_dict = {}

for index, num in enumerate(nums):
    complement = target - num
    if complement in my_dict:
        print([my_dict[complement], index])
        break
    my_dict[num] = index