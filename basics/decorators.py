
def smartDiv(func):
    f=5
    def inner(a,b):
        # f = f+5
        print(f)
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

