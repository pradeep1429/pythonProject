import inspect
from functools import wraps


# Python3 compatible code (it runs fine under python2 too).
def initializer(fun):
    names, varargs, keywords, defaults = inspect.getargspec(fun)

    @wraps(fun)
    def wrapper(self, *args, **kargs):
        for name, arg in zip(names[1:], args) + kargs.items():
            setattr(self, name, arg)
        for i in range(len(defaults)):
            index = -(i + 1)
            if not hasattr(self, names[index]):
                setattr(self, names[index], defaults[index])
        fun(self, *args, **kargs)

    return wrapper


class Foo(object):
    @initializer
    def __init__(self, a, b, c=None, d=None, e=3):
        pass


f = Foo(1, 2, d="a")
assert f.a == 1
assert f.b == 2
assert f.c is None
assert f.d == "a"
assert f.e == 3

