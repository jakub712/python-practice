text = "Mastery takes time"
text = text.split()
text[0] = text[0] [::-1]
print(text[0])
text[1] = text[1] [::-1]
print(text[1])
text[2] = text[2] [::-1]
print(text[2])

new_text = text[0] +  " " + text [1] + " " + text[2]

print(new_text)