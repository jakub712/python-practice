temps = [25, 36, 30, 21, 38, 33, 18]
humidity = [40, 45, 55, 48, 35, 80, 60]
dangerous = False

for i in range (len(temps)):
    if (temps [i] > 35 and humidity [i] > 70) or (temps [i] < 20 and humidity [i]< 50):
        dangerous = True
        break

if dangerous:
    print ("Dangerous weather detected")
else:
    print("conditions acceptable")