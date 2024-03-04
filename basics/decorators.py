import configparser


def smartDiv(func):
    def inner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return inner



@smartDiv
def div(a,b):
    print(a//b)

div(2,4)

def changeCase(func):
    def inner(text):
        return func(repr(text).swapcase())
    return inner

@changeCase
def updateCase(value):
    print(value)

updateCase("PRADEEP")
updateCase("pradeep")

def eqdecor(func):
    def inner(text):
        print("==========")
        func(text)
        print("==========")
    return inner

def dashdecor(func):
    def inner(text):
        print("----------")
        func(text)
        print("----------")
    return inner

@eqdecor
def pattern(value):
    print(value)

pattern("pradeep")


def ini_loader(section):
    def decorator(func):
        def wrapper(*args, **kwargs):
            parser = configparser.ConfigParser()
            parser.read("C:\\Users\\Pradeep_Avadhanam\\Workspace\\pythonProject\\data.ini")
            kwargs[section] = dict(parser.items(section))
            return func(*args, **kwargs)
        return wrapper
    return decorator
# def read_ini(decorated_function,section):
#     def wrapper_function(*args, **kwargs):
#         config = configparser.ConfigParser()
#         config.read("C:\\Users\\Pradeep_Avadhanam\\Workspace\\pythonProject\\data.ini")
#
#         return decorated_function(config, *args, **kwargs)
#     return wrapper_function

@ini_loader('common')
def get_web_server_host(common):
    return common.get('browser')

print(get_web_server_host())
