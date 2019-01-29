# get two integers from the user
divident = int(input('Please enter the number to divide: '))
divisor = int(input('Please enter the divident: '))
# if possible divide them and report the result
if divisor != 0:
    quotient = divident/divisor
    print(divident, '/', divisor, '=', quotient)
print('Program finished')
