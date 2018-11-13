def hello(name='world'):
    return 'Hello=== %(name)s' % dict(name=name)

if __name__ == '__main__':
    print(hello())


