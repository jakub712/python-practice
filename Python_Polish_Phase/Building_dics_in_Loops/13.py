# 🔁 Challenge: invert_dict
# 
# You're given a dictionary where each key maps to a unique value.
# Invert it so that each value becomes a key, and the original key becomes its value.
#
# Example:
# invert_dict({'a': 1, 'b': 2, 'c': 3}) ➞ {1: 'a', 2: 'b', 3: 'c'}

def invert_dict(d: dict) -> dict:
    my_dict = {}

    for key, value in d.items():
        my_dict[value] = key

    return my_dict
# Test
print(invert_dict({'a': 1, 'b': 2, 'c': 3}))
# Expected: {1: 'a', 2: 'b', 3: 'c'}
