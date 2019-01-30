# abuse for
for i in range(10):
    print(i, end=' ')
    if i == 5:
        i = 20
    print('({0})'.format(i), end=' ')
print()
