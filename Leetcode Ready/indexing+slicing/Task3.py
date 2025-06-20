#you are given a word if the length is odd print the middle number
# if even print the two middle numbers. 
word = "Cat"

x = int(len(word)/2)


if len(word) % 2 == 0:
    print (word[x-1:x+1])
else:
    print (word[x])