import sys


class parent:

    def __init__(self):
        print("in parent init")

    def feature1(self):
        print("feature1")
    def feature2(self):
        print("feature2")

class child1(parent):
    def __init__(self):
        super().__init__()
        print("in child init")

    def feature3(self):
        print("feature3")
    def feature4(self):
        print("feature4")

# obj = child1()

class A(parent):
    def __init__(self):
        super().__init__()
        print("in A init")

    def feature1(self):
        print("feature1A")
    def feature2(self):
        print("feature2A")

class B(parent):
    def __init__(self):
        super().__init__()
        print("in B init")

    def feature1(self):
        print("feature3B")
    def feature4(self):
        print("feature4B")
class D(parent):
    def __init__(self):
        # super().__init__()
        print("in D init")

    def feature1(self):
        print("feature1D")
    def feature2(self):
        print("feature2D")
class C(B,A,D): #Method Resolution Order(MRO)
    def __init__(self):
        super().__init__()
        print("in C init")

    def feature1(self):
        super().feature1()

        
obj = C()
# obj.feature1()


