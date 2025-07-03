# Given a list of (author, book_title) pairs, return a dictionary
# mapping each author to a list of their books.

def group_books(pairs):
    result = {}
    for key, value in pairs:
        if key not in result:
            result[key] = []
        result[key].append(value)
    return result

print(group_books([
    ("Orwell", "1984"),
    ("Tolkien", "The Hobbit"),
    ("Orwell", "Animal Farm"),
    ("Tolkien", "LOTR"),
    ("Rowling", "Harry Potter"),
]))
# Expected: {'Orwell': ['1984', 'Animal Farm'], 'Tolkien': ['The Hobbit', 'LOTR'], 'Rowling': ['Harry Potter']}
