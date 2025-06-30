numbers = [1, 2, 3, 4, 5, 6]
# Your task: Use list comprehension to get only the even numbers from the list.

evens = [num for num in numbers if num % 2 == 0]

print(evens)