# Given a list of (type, animal) pairs, return a dictionary
# mapping each animal type to a list of animals in that group.

def group_animals(pairs):
    result = {}
    for key, value in pairs:
        if key not in result:
            result[key] = []
        result[key].append(value)
    return result

print(group_animals([
    ("mammal", "dog"),
    ("bird", "sparrow"),
    ("mammal", "cat"),
    ("bird", "eagle"),
    ("reptile", "lizard"),
]))
# Expected: {'mammal': ['dog', 'cat'], 'bird': ['sparrow', 'eagle'], 'reptile': ['lizard']}

