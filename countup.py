count = 0
entry = 'Y'

while entry != 'N' and entry != 'n':
    print(count)
    entry = input('Please enter "Y" to continue or "N" to quit: ')
    if entry == 'Y' or entry == 'y':
        count += 1
    elif entry != 'N' and entry != 'n':
        print('"' + entry + '" is not a valid choice')
