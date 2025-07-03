def collect_values(pairs):
    result = {}

    for key, value in pairs:
        if key not in result:
            result[key] = []         # only create list ONCE per key
        result[key].append(value)    # then always append to it

    return result

print(collect_values([('a', 1), ('b', 2), ('a', 3)]))
# Expected: {'a': [1, 3], 'b': [2]}

##wtttttfff