import math 
#From 1 to 500, print every number that is a square (like 4, 9, 16...).
#Check if math.sqrt(n).is_integer().

for i in range (1, 501):
    if math.sqrt(i).is_interger():
        print(i)