d1 = 1.11 - 1.10
d2 = 2.11 - 2.10
print('d1 =', d1, ' d2 =', d2)
diff = d1 - d2
if diff < 0:
    diff = -diff
if diff < 0.0000001:
    print('Same')
else:
    print('Different')
