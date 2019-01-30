# computesquareroot.py

val = float(input('Enter number: '))
root = 1.0

diff = root*root - val

while diff > 0.00000001 or diff < -0.00000001:
    print(root, 'squared is', root*root)
    root = (root + val/root) / 2
    diff = root*root - val

print('Square root of', val, '=', root)
