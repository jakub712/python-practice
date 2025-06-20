#Boolean Logic Question (no loop this time)

#Scenario:
#You're setting up a home automation system. You want to trigger an override if:

#    The lights are off and it's after 10 PM

#    Or the security system is disarmed and the door is open

#Write the Python code using Boolean variables:

#lights_on = False
#hour = 23  # 24-hour format
#security_armed = False
#door_open = True

#Trigger an override if the conditions are met and print "OVERRIDE TRIGGERED" or "System Normal".

lights_on = False
hour = 23  # 24-hour format
security_armed = False
door_open = True

overide = False

if (not lights_on and hour > 22) or (not security_armed and door_open):
    overide = (True)


if overide:
    print(True)
else:
    print(False)

#well that was easy