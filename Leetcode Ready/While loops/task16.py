#Case Insensitive

#Make the check ignore case. "Level" should return True.

#    Use .lower() on both characters.

word = "Level"
word = word.lower()

left = 0 
right = len(word) -1
i = 0

while left < right:
    if word[left] != word[right]:
        print (False)
        break
    left += 1
    right -= 1
else:
    print(True)

