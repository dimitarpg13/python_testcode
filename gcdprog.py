num1 = int(input('Please enter an integer: '))
num2 = int(input('Please enter another integer: '))

# determine the smaller of num1 and num2 
min = num1 if num1 < num2 else num2

largest_factor = 1

for i in range(1, min + 1):
    if num1 % i == 0 and num2 % i == 0:
        largest_factor = i

print(largest_factor)
