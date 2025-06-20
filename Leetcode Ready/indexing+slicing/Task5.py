# you are given a wand. create a new word that is the original + its reverse
# eg "code" -> "codeedoc"

word = "Klaudija"
word = word.lower()

original = word
flipped = word[::-1]

print( original + flipped)