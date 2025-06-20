temps = [22, 39, 41, 28, 19, 24, 31]
humidity = [60, 85, 90, 55, 65, 70, 50]
uv_index = [5, 6, 9, 7, 4, 8, 3]
dangerous = False

for i in range (len(temps)):
    if (temps[i] > 38 and humidity [i] > 80) or (uv_index [i] > 8 and temps [i] > 30):
        dangerous = True
        break

if dangerous:
    print ("⚠️ Extreme weather alert triggered")
else:
    print("✅ All conditions safe")