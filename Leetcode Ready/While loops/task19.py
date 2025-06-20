#Task 4 – Word-Only Palindrome

#Goal:
#Ignore numbers, ignore punctuation—only check the letters.
def valid_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            # Mismatch found — try skipping one char from either side
            i, j = left + 1, right
            while i < j and s[i] == s[j]:
                i += 1
                j -= 1
            if i >= j:
                return True

            i, j = left, right - 1
            while i < j and s[i] == s[j]:
                i += 1
                j -= 1
            return i >= j
        else:
            left += 1
            right -= 1

    return True





print(valid_palindrome("abca"))      # True
print(valid_palindrome("racecar"))   # True
print(valid_palindrome("abcdef"))    # False


#while left < right:
#if word[left] != word[right]:
#    left += 1
#    if word[left] != word[right]:
#        right -= 1
#        if word[left] != word[right]:
#            print(Fail)
#else:
#    print(True)