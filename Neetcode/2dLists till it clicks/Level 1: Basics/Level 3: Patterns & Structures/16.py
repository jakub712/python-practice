### 🔥 Q17: Two Sum


nums = [2, 11, 15, 7]
target = 9
# Step-by-step:
# 1. Create an empty dictionary.
# 2. Loop through nums with index.
# 3. Calculate complement = target - num.
# 4. If complement in dictionary, return indices.
# 5. Else add num:index to dictionary.
my_dict = {}

for index, num in enumerate(nums):
    complement = target - num
    if complement in my_dict:
        print([my_dict[complement], index])
        break
    my_dict[num] = index
#thxs chat gpt!