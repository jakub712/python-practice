def build_hash_set(keys):
    # your code here
    hash_set = set()
    for key in keys:
        if key not in hash_set:
            hash_set.add(key)
        else:
            pass
    return hash_set


print(build_hash_set(['a', 'b', 'a']))  # should print {'a', 'b'}
