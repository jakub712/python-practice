# Input:
letters = ['x', 'y', 'z']
# Add key 'item' with value as letter, using loop (one at a time)
# Output: {'item': 'z'}
value = 'item'
result={}

for letter in letters:
    result['item'] = letter
    print(result)
