# Q6. Count how many times each letter appears in the string "banana".
my_s = "banana"

counter = {}

for i in my_s:
    if i in counter:
        counter [i]+=1 
    else:
        counter [i] =1

print(counter)