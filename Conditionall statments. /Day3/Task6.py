#Print all numbers from 1 to 100, but skip every number that ends in 7.
#Hint: Use if i % 10 == 7: continue.

for i in range(1, 101, 1):
    if i % 10 ==  7: continue
    print(i)