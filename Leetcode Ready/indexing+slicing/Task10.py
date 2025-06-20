#hidden messege print only the letters that are in an even index and are uppercase.
text = "heLLo ThEre ProGrAMMEr"
#output ->"LTEPME

text = text[::2]
upper =""

for char in text:
    if char.isupper():
        upper += char
print(upper)

