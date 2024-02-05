

a = 10
def something():
    a = 24
    print(globals()['a'])
    print(a)
    globals()['a'] = 29



something()
print(a)
print(__name__)
print(__doc__)
print(__file__)
