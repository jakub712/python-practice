#Ask the user for a number. Keep looping until they enter a number between 1 and 10.
#Use while + if.
num = int(input("Pick any Number! " ))

while num:  #had no idea you could just write while num: i thought some conditions were needed. 
    print("Pick a Smaller Number")
    if num < 10 and num > 0:
        print("Your Number is between 1 and 10!")
    else:
        print("Pick a Bigger Number")
    break