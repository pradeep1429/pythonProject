# Generators are useful when we want to produce a large sequence of values, but we don't want to store all of them in memory at once.
def fib(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


x = fib(4)


print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))

# Using @property decorator
class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value...")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value


# create an object
human = Celsius(37)

print(human.temperature)

print(human.to_fahrenheit())

# coldest_thing = Celsius(-300)


