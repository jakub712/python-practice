words = ["python", "java", "python", "c++", "python", "java"]
#Use a loop to build a dictionary that counts how many times each word appears.
counter = {}

for key in words:
    if key in counter:
        counter[key] +=1
    else:
        counter[key] = 1

print(counter)