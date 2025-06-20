word_count = 0
num_count = 0
sen = input("Write a sentance with at least 2 seperate numbers! ")

#cleaning
cleaned = ""
for char in sen:
    if char.isalnum() or char == " ":
        cleaned += char

# making the sentance to a list
x = cleaned.split()

#num and word count
for i in x:
    if i.isdigit():
        num_count +=1
    else:
        word_count +=1



#num and word percentage
percentage = (word_count) + (num_count)
word_percentage = (word_count) / percentage
word_percentage = round (word_percentage, 1) * 100

num_percentage = (num_count) / percentage
num_percentage = round (num_percentage, 1)
num_percentage = num_percentage * 100

#cleaning out nums.
clean = ""
for char in sen:
    if char.isalpha() or char == " ":
        clean += char

y = clean.split()

# amount of letters
amount = 0
for i in y:
    amount += len(i)

avaredge_word_length = (amount / word_count)
avaredge_word_length = round(avaredge_word_length, 2)

#finding the longest word. 
longest=""
for i in y:
    if len (i) > len(longest): 
        longest = i
    else:
        continue


print (f"""
📝 Text Analysis Complete!
--------------------------
Total words: {word_count}
Total numbers: {num_count}

Word percentage: {word_percentage}
Number percentage: {num_percentage}

Longest word: {longest}
Average word length: {avaredge_word_length}
--------------------------
""")

#  Well, I bought 3 apples, 2 bananas, and $5 worth of... something???  
