def last_value(pairs):
    result = {}
    for key, value in pairs:
        result[key] = value
    return result

# Test it:
print(last_value([('a', 1), ('b', 2), ('a', 3)]))
# Expected: {'a': 3, 'b': 2}
