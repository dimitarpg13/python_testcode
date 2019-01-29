# prompt user for temperature to convert and read the supplied vaue
degreesF = float(input('Enter the temperature in degrees F: '))
# perform the conversion
degreesC = (degreesF - 32.0)*5.0/9.0
# report the result
print(degreesF, 'degrees F =', degreesC, 'degrees C')
print(degreesC)
