
# A Closure in Python is a function object that has access to variables from its enclosed lexical scope,
# even when the function is called outside of that scope. This means the function remembers the values
# in its enclosing lexical scope even if they are not present in memory.
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

closure = outer_function(10) # Here closure is our inner_function and it's a closure.
print(closure)
print(closure(5))  # Output: 15, as it remembers x = 10 from its enclosed scope.