# get two integers from the user
divident = int(input('Please enter the number to divide: '))
divisor = int(input('Please enter divident: '))
# if possible divde them and report the result
if divisor != 0:
    print(divident, '/', divisor, '=', divident/divisor)
else:
    print('Division by zero is not allowed')
