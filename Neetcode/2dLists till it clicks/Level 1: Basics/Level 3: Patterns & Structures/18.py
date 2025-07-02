nums = [1, 1, 1]
target = 2
# Count the number of continuous subarrays that sum to target.
my_dict = {}

for index, num in enumerate(nums):
    complement = target - num
    if complement in my_dict:
        print([my_dict[complement], index])
        break
    my_dict[num] = index