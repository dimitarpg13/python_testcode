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
