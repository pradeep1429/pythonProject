
class Functions:

    def isPrime(x):
        if x in [2, 3]:
            return True
        if(x == 1) or (x % 2 == 0):
            return False
        y = 3
        while y * y <= x:
            if x % y == 0:
                return False
            y += 2
        return True

    print(isPrime(79))


    def arguments(*argsv):
        for arg in argsv:
            print(arg, end=" ")

    arguments("python", "learning", "in", 8, "weeks")

    def kwarguments(**kwargs):
        for key,value in kwargs.items():
            print("{} == {}".format(key, value))

    kwarguments(a='python',b='learning',c='8weeks')


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(10))


def update(x):
    print(id(x))


a = 10
print(id(a))
update(a)
update(10)

def outer_function():
    num = 20

    def inner_function():
        global num
        num = 25

    print("Before calling inner_function(): ", num)
    inner_function()
    print("After calling inner_function(): ", num)


outer_function()
print("Outside both function: ", num)

