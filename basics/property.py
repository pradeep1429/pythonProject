#Python's @property decorator is used to specify a method in the class to be a "getter" function of a class attribute.
# The @<attribute>.setter decorator is used to specify a method as a "setter" function of a class attribute
#In this example, the @property decorator makes the 'scores' method a "getter" for the 'scores' property.
#So, you can access it like .scores instead of .scores().
#The @scores.setter decorator makes the full_name method a "setter" for the full_name property.

class sport:
    def __init__(self):
        self.wins = 0
        self.loses = 0

    def wons(self):
        self.wins += 1

    def losses(self):
        self.loses -= 1

    @property
    def scores(self):
        return self.wins - self.loses


s = sport()
s.wons()
scr = int(s.scores)
print(scr)

class Circle:
    def __init__(self, radius):
        self._radius = radius
    @property
    def radius(self):
        return self._radius
    @radius.setter
    def radius(self, value):
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Radius must be positive")
crc = Circle()
print(crc.radius)