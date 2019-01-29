seconds_per_minute = 60
seconds_per_hour = 60*seconds_per_minute  # 3600

# get user input in seconds
seconds = int(input("Please enter the number of seconds:"))

# first, compute the number of hours in the given number of seconds
hours = seconds // seconds_per_hour 

seconds = seconds % seconds_per_hour

minutes = seconds // seconds_per_minute

seconds = seconds % seconds_per_minute

print(hours, end='')

if hours == 1:
    print(" hour ", end='')
else:
    print(" hours ", end='')

print (minutes, end='')

if minutes == 1:
    print(" minute ", end='')
else:
    print(" minutes ", end='')

print (seconds, end='')
# decide between singular and plural form of seconds
if seconds == 1:
    print(" second")
else:
    print(" seconds")

