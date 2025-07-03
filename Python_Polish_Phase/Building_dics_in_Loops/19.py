# ❓ Given a list of (class_name, student_name) pairs,
# return a dictionary grouping all students by their class.
# Use .get()

def group_students(pairs):
    result = {}
    for key, value in pairs:
        result[key] = result.get(key, []) + [value]

    return result

# Test
print(group_students([
    ("Math", "Alice"),
    ("Science", "Bob"),
    ("Math", "Charlie"),
    ("History", "Diana"),
    ("Science", "Eve")
]))
# Expected: {'Math': ['Alice', 'Charlie'], 'Science': ['Bob', 'Eve'], 'History': ['Diana']}
