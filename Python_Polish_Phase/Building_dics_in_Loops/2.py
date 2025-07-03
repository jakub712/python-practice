
words = ["a", "b", "a", "c", "b", "d"]
first_seen = {}
#Build a dictionary that records the first index each word appears at.
for key, value in enumerate(words):
    if value not in first_seen:
        first_seen[value] = key

print(first_seen)
