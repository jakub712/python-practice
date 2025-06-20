wind_speeds = [10, 12, 15, 16, 30, 14, 18, 19, 22, 40, 17, 12, 9, 8]
warning = False

for i in wind_speeds:
    if i > 35 or i < 10:
        warning = True
        break

if warning:
    print("Storm warning triggered")
else:
    print("All conditions normall.")