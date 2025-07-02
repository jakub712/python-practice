
### 🔥 Q16: Check for Duplicates in List

nums = [1, 2, 3, 4, 5, 2]
# Step-by-step:
# 1. Create an empty set.
# 2. Loop through nums.
# 3. If num in set, return True.
# 4. Else add num to set.
# 5. Return False if loop completes.
nset= {}

for num in nums: 
    nset[num] = nset.get(num, 0) +1
    
if 2 in nset:
    print(True)
else:
    print(False)