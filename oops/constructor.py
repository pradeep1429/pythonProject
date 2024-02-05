class Person:
    def __init__(self):
        self.name = "Pradeep"
        self.age = 25

    def __eq__(self, other):
        if self.age == other.age:
            return True
        else:
            return False


per1 = Person()
per2 = Person()
per2.age = 34
if per1.__eq__(per2):
    print("age is same")
else:
    print("age is different")
