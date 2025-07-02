nums = [10, 5, 3, 4, 3, 5, 6]
target = 9 
my_dict = {}

for index, num in enumerate(nums):
    complement = target - num
    if complement in my_dict:
        print([my_dict[complement], index])
        break
    my_dict[num] = index