# request input from the user
num = int(input("Please enter an integer in the range 0...9999: "))

# attenuate the number if necessary
if num < 0: # make sure the number is not too small
    num = 0
if num > 9999:
    num = 9999

print(end="[")

# extract and print thousands-place digit
digit = num//1000
print(digit, end="")
num %= 1000

digit = num//100
print(digit, end="")
num %= 100

digit = num//10
print(digit, end="")
num %= 10

print(num, end="")

print("]")
