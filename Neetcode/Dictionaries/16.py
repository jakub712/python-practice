# Q4. Safely access a missing key in a dict with .get()
profile = {"name": "Jack"}
# Print "N/A" if "email" is missing
x = profile.get('email')
if x == None:
    print("N/A")
else:
    print(x)

