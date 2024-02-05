
# arg1 and arg2 are standard positional arguments.
# *args is used to take any number of extra positional arguments.
# kwarg1 and kwarg2 are keyword-only arguments with default values.
# **kwargs is used to take any number of extra keyword arguments.
# the arguments must be defined in this order:
# standard positional arguments,
# arbitrarily many positional (*args),
# keyword-only arguments
# arbitrary keyword arguments (**kwargs).
def argSequence(arg1, arg2, *args, kwarg1="Hello", kwarg2="World", **kwargs):
    print(f"arg1: {arg1}")
    print(f"arg2: {arg2}")
    for i, arg in enumerate(args):
        print(f"arg {i+3}: {arg}")
    print(f"kwarg1: {kwarg1}")
    print(f"kwarg2: {kwarg2}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

argSequence(1, 2, 3, 4, 5, kwarg1="Greetings,", extra1="extra", extra2="arguments")
