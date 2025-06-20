temps = [22, 37, 19, 30, 25, 18, 36]
wind_speeds = [10, 32, 15, 12, 20, 8, 35]
humidity = [40, 45, 55, 48, 35, 60, 30]

danger = False

for i in range(len(temps)):
    if (temps [i]> 35 and wind_speeds [i]> 30 ) or (temps[i] < 20 and humidity [i]> 50):
        danger = True
        break

if danger:
    print( "Severe weather warning")
else:
    print( "Weather stable")