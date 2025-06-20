word ="racecanr"  #first time doing this without needing any help at all! took me two days!
l = 0
r = len(word) -1

while l < r:
    if word[l] != word[r]:
        a, b = l +1, r
        while a < b and word[a] == word[b]:
            a +=1
            b -=1
        if a >= b:
            print(True)
            break

        a,b = l, r-1
        while a < b and word[a] == word[b]:
            a +=1
            b -=1
        if a >= b:
            print(True)
        else:
            print(False)
        break
    else:
        l += 1
        r -=1
else:
    print(True)