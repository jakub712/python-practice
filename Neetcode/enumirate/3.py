# 8. Find index of first 'apple'
fruits = ['banana', 'orange', 'apple', 'grape']
for i, fruit in enumerate(fruits):
    if fruit == 'apple':
        print(i)  # prints 2
        break
