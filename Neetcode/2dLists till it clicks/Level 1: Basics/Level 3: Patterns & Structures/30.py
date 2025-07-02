nums = [1, 7, 5, 9, 2, 12, 3]
k = 3
my_dict = {}

for index, num in enumerate(nums):
    complement = k - num
    if complement in my_dict:
        print([my_dict[complement], index])
        break
    my_dict[num] = index