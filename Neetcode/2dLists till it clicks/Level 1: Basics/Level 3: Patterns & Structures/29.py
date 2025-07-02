nums = [1, 7, 5, 9, 2, 12, 3]
target = 19
my_dict = {}

for index, num in enumerate(nums):
    complement = target - num
    if complement in my_dict:
        print([my_dict[complement], index])
        break
    my_dict[num] = index