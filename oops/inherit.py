class A():
    def __init__(self,x,y):
        print("in A init")

    def feature1(self):
        print("feature1A")

    def feature2(self):
        print("feature2A")
class D():
    def __init__(self):
        super().__init__()
        print("in D init")

    def feature1(self):
        print("feature3D")

    def feature4(self):
        print("feature4D")

class B():
    def __init__(self):
        super().__init__()
        print("in B init")

    def feature1(self):
        print("feature3B")

    def feature4(self):
        print("feature4B")




class C(A,B,D):  # Method Resolution Order(MRO)
    def __init__(self):
        super().__init__("ds","dss")
        print("in C init")

    def feature1(self):
        super().feature1()


obj = C()