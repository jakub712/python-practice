temps = [25, 28, 32, 18, 30, 22, 26]

unsafe = False
for i in temps:
    if i > 35 or i < 20:
        unsafe = True
        break

if unsafe:
    print("Warning: Unsafe day")
else:
    print("All temperatures safe")
