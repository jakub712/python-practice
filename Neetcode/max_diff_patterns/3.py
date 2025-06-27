# ⏱ 4 min
# 3. Track the largest positive adjacent difference (ignore negative diffs)

nums = [20, 17, 25, 10, 30]
# Output: 20
max_diff = float('-inf')

for i in range(len(nums)-1):
    diff = nums[i + 1] - nums [i]
    if diff > 0:
        max_diff = max(max_diff, diff)
    else:
        continue
print(max_diff)
