# Q7. Use .get() to handle missing keys in nested dictionaries.
data = {
    "user": {
        "name": "Jane"
    }
}
# Safely get "age", default to "Unknown"

age = data["user"].get("age", "Unknown")
print(data)