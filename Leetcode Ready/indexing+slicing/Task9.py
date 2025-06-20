#Task 9: word flip at middle
#You are given a word. split it into two halves return the seccond half then first.
#word = "Example"
#output = "pleexam"

word = "pretty"

x = int(len(word)/2)
left =(word[0:x])
word += "s"
right = (word[x:-1])

print(right + left)