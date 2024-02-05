# program to illustrate access modifiers of a class

# super class
class parent:
    # public data member
    var1 = None

    # protected data member
    _var2 = None

    # private data member
    __var3 = None

    # constructor
    def __init__(self, var1, var2, var3):
        self.var1 = var1
        self._var2 = var2
        self.__var3 = var3

    # public member function
    def displayPublicMembers(self):
        # accessing public data members
        print("Public Data Member: ", self.var1)

    # protected member function
    def _displayProtectedMembers(self):
        # accessing protected data members
        print("Protected Data Member: ", self._var2)

    # private member function
    def __displayPrivateMembers(self):
        # accessing private data members
        print("Private Data Member: ", self.__var3)

    # public member function
    def accessPrivateMembers(self):
        # accessing private member function
        self.__displayPrivateMembers()


# derived class
class child(parent):

    # constructor
    def __init__(self, var1, var2, var3):
        parent.__init__(self, var1, var2, var3)

    # public member function
    def accessProtectedMembers(self):
        # accessing protected member functions of super class
        self._displayProtectedMembers()


# creating objects of class
obj = child("Geeks", 5, "Geeks !")
obj1 = parent("python", 4, "incubation !")

# calling public member functions of the class
obj.displayPublicMembers()
obj.accessProtectedMembers()
obj.accessPrivateMembers()

print(f'class is accessing protected data member: {child._var2} {parent._var2}')

# Object can access protected member
print(f'parent object is accessing protected variable: {obj1._var2}')
print(f'child object is accessing protected variable: {obj._var2}')
obj1.__var3 = "pradeep"
print(obj1.__var3)

# these private members are not strictly private. However, Object can access private member in alternate way
print(f'object is accessing private variable: {obj._parent__var3} {obj1._parent__var3}')

# object can not access private member, so it will generate Attribute error
# print(obj.__var3)
