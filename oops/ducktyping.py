class student1:
    def school(self):
        print("school1")

class student2:
    def school(self):
        print("school2")

class test:
    def center(self, s):
        s.school()

s = student2()
t = test()
t.center(s)