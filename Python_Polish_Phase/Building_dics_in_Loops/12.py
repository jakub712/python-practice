# 🔁 Challenge: check_keys
# 
# Write a function that takes:
# - a set of keys (called hash_set)
# - a list of keys to check (called keys)
# 
# Return a list of booleans — True if the key is in the set, False if not.
# 
# Example:
# check_keys({'a', 'b', 'c'}, ['a', 'x', 'c']) ➞ [True, False, True]

def check_keys(hash_set, keys):
    x = []
    for key in keys:
        if key in hash_set:
            x.append(True)
        else:
            x.append(False)
    
    return x
# Test case
print(check_keys({'a', 'b', 'c'}, ['a', 'x', 'c']))  # Expected: [True, False, True]
