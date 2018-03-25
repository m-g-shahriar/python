import datetime

time=datetime.datetime.now()
print("Current Date and time 24 hour")
#for 24 hour
print(time.strftime("%Y-%m-%d %H:%M:%S"))

#for 12 hour
print("\n")
print("12 hour")
print(time.strftime("%Y-%m-%d %I:%M:%S"))