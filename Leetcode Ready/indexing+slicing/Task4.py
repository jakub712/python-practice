#You are given a full name like Sarah Conner generate a username made from:
#the first 3 letters pf the first name, last name and all lowercase. 

name = "Klaudija Jenciute"
name = name.lower()
name= name.split()
fname = name[0] 
fname = fname [0: 3]
lname = name[1]
lname = lname[0: 3]
username = fname + lname 
print(username)
