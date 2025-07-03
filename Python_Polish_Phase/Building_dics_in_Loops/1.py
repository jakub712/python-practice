words = ["a", "b", "c"]
my_dict = {}
for i, word in enumerate(words):
    my_dict[word] = my_dict.get(word, i)

print(my_dict)