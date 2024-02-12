# When using a name in a function and Python needs to determine its value,
# Python looks up the name using the LEGB rule: It first looks in the local scope,
# then, from inside out, all enclosing functions' scopes,
# then the global scope, and finally the built-in scope.
# If a variable is not found in any scope, a NameError is raised.


x = 10  # Global variable
class Legb:
    def __init__(self):
        global x
        x = 46
        print(x, id(x))
    def func(self):
        x = 20  # Local variable
        print("Local : ", x, id(x))
        # nonlocal var1 --> You can’t use a nonlocal statement in either the global scope or in a local scope

        def inner_func():
            nonlocal x
            x = 30  # Changes the local variable of the outer function
            print("Nonlocal : ", x, id(x))


        inner_func()
        var = 23
        print(var)


l = Legb()
print(l.func())
print("Global : ", x,id(x))

