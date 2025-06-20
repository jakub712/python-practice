#Task 8- Index Map Rebuilder. your given a word and indecies your job is to make a new string collecting the characters at those indecies
# word = "masterpiece" indecies = [0, 2, 4, 6, 8]
#output = "msepe"

word = "masterpiece"
indicies = [0, 2, 4, 6, 8]
new = ""
for i in indicies:
    new += word[i]

print(new)