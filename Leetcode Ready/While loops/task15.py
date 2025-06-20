#Input:  "xxabcddcbazyyracecarnomirrorabbaxyz"

#Goal: Print the **longest** palindrome (e.g. "abcddcba")
#No slicing, no reverse strings. Use loops.

text = "xxabcddcbazyyracecarnomirrorabbaxyz"
longest = ""

i = 0
while i < len(text):
    # Odd-length palindrome (centered at i)
    left = i
    right = i
    while left >= 0 and right < len(text) and text[left] == text[right]:
        if (right - left + 1) > len(longest):
            longest = text[left:right+1]
        left -= 1
        right += 1

    # Even-length palindrome (centered between i and i+1)
    left = i
    right = i + 1
    while left >= 0 and right < len(text) and text[left] == text[right]:
        if (right - left + 1) > len(longest):
            longest = text[left:right+1]
        left -= 1
        right += 1

    i += 1

print(longest)
#yeah i can't do this shit yet chat gpt helped.