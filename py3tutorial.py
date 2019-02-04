def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))

def concat(*args, sep="/"):
    return sep.join(args)


def strings_test1():
    a = str(b'Zoot!')
    print('a = str(b\'Zoot!\')')
    print('a={0}'.format(a))
    b = '01\t012\t0123\t01234'
    print('b = \'01\\t012\\t0123\\t01234\'')
    print('b={0}'.format(b))
    print('b.expandtabs()={0}', b.expandtabs());
    c = str('Python')
    print('\'Py\' in \'Python\' = {0}'.format('Py' in 'Python'))

def unpackargs():
    l1 = list(range(3,6))
    print('l1 = list(range(3,6))')
    print('l1={0}'.format(l1))
    args = [3, 6]
    l2 = list(range(*args))
    print('l2 = list(range(*args))')
    print('l2={0}'.format(l2))

def make_incrementor(n):
    return lambda x: x + n

def incr_lambda():
    f = make_incrementor(42)
    print('f(0)={0}'.format(f(0)))
    print('f(1)={0}'.format(f(1)))
