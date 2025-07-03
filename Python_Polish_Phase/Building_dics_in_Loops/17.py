# Given a list of (class_name, student_name) pairs, return a dictionary
# mapping each class to a list of enrolled students.

def group_students(pairs):
    result = {}
    for key, value in pairs:
        if key not in result:
            result[key] = []
        result[key].append(value)

    return result

print(group_students([
    ("Math", "Alice"),
    ("Science", "Bob"),
    ("Math", "Charlie"),
    ("History", "Diana"),
    ("Science", "Eve"),
]))
# Expected: {'Math': ['Alice', 'Charlie'], 'Science': ['Bob', 'Eve'], 'History': ['Diana']}
