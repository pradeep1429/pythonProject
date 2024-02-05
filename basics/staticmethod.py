
from datetime import date


class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	@classmethod
	def fromBirthYear(cls, name, year):
		return cls(name, date.today().year - year)

	@staticmethod
	def isAdult(age):
		return age > 18


person1 = Person("fsg",23)
person2 = Person("adfa",18)
person3 = Person.fromBirthYear("abc",1989)
print(person1.age)
print(person2.age)
print(person3.age)

print(Person.isAdult(person1.age))
print(Person.isAdult(person2.age))
print(Person.isAdult(person3.age))
