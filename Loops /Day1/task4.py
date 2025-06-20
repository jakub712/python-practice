 #4. Count How Many Times "a" Appears in a String
#Write a function that takes a string and returns the number of lowercase 'a' letters in it.
#did this on lunch break starting to get the hang of it but im still not there yet.
def count_a(text):
    counter = 0
    for i in text:
        if i =="a":
            counter += 1
    print(counter)



count_a("banana")
count_a("Python")
#example
#count_a("banana") → 3
#count_a("Python") → 0


