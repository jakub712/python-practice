# ❓ Given a list of words, group them by their starting letter.
# Use .get()

def group_by_first_letter(words):
    result = {}
    for key, value in words:
        result[key] = result.get(key, []) + [value]
    # Your code here

    return result

# Test
print(group_by_first_letter(["cat", "car", "apple", "bat", "ball", "ant"]))
# Expected: {'c': ['cat', 'car'], 'a': ['apple', 'ant'], 'b': ['bat', 'ball']}
