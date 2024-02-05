import _pytest
import pytest


class student:
    school = "python"
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def average(self):
        return (self.m1 + self.m2 + self.m3) / 3

    @classmethod
    def getSchl(cls):
        return cls.school;
    @staticmethod
    def info():
        print("static method is not related to class/object. "
              "so dont require self or object to pass")

s1 = student(34,67,82)
s2 = student(56,78,90)
s3 = student(60,89,56)

print(s1.average())
print(s2.average())
print(s3.average())
print(student.getSchl())
s1.info()