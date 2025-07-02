nums = [1, 2, 3, 2, 3, 4]
target = 7 
my_dict = {}

for index, num in enumerate(nums):
    complement = target - num
    if complement in my_dict:
        print([my_dict[complement], index])
        break
    my_dict[num] = index