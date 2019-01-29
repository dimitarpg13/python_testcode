divident = int(input('Enter divident: '))
divisor = int(input('Enter divisor: '))

msg = divident/divisor if divisor != 0 else 'Error, cannot divide by zero'
print(msg)
