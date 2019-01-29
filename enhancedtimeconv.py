# enhancedtimeconv.py


# get the number of seconds
seconds = int(input("Please enter the number of seconds:"))

# first compute the number of hours in the given number of seconds
hours = seconds // 3600

#next compute the number of minutes in the remaining number of seconds
minutes = seconds // 60

seconds = seconds % 60

print(hours, ":", sep="", end="")

tens = minutes // 10

ones = minutes % 10
print(tens, ones, ":", sep="", end="")

tens = seconds // 10

ones = seconds % 10
print(tens, ones, sep="")
