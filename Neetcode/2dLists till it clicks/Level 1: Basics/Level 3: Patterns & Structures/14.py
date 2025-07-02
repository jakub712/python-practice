### 🔥 Q15: Check Anagrams

s1 = "listen"
s2 = "silent"
# Step-by-step:
# 1. Count characters in s1 using a dictionary.
# 2. Count characters in s2 using a dictionary.
# 3. Compare the two dictionaries.
# 4. Return True if equal, else False.
rs1 = {}
rs2 = {}

for letter in s1:
    rs1[letter] = rs1.get(letter, 0) +1

for letter in s2:
    rs2[letter] = rs2.get(letter, 0) +1

print(rs1 == rs2)