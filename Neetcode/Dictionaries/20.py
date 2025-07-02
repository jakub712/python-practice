# Q8. Add up the total price from a list of items using .get()
cart = [
    {"name": "apple", "price": 2},
    {"name": "banana"},  # no price!
    {"name": "milk", "price": 3}
]
# Use .get("price", 0) to avoid crash
result = 0
for item in cart:
    result += item.get("price", 0)

print(result)


