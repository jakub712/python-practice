nums = [2,7,11,15]
target = 9
output = [0,0]
l = 0 
r = len(nums) -1
while l < r:
    if (nums[l] + nums[r]) != target:
        a, b = l +1, r
        while a < b and nums[a] + nums[b] == target:
            x = nums.index(a)
            y = nums.index(b)
            output = [x,y]

        print(output)