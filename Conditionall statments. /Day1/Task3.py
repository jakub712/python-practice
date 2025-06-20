#Task 3: Check Password
#Ask for a password. If it matches "letmein", print "Access granted". Else, "Access denied".

password = ("letmein")
attempt = input("What is the password?")
if attempt == password:
    print("Access granted")
else:
    print("Access denied")