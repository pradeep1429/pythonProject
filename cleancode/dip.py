class Lamp:
    def start(self):
        return 'Lamp is On...'

class Room:
    def __init__(self):
        self.lamp = Lamp()

    def glow(self):
        return self.lamp.start()

rm = Room()
print(rm.glow())
# 'Room' is a high-level class that depends on 'Lamp', a low-level class.
# If you want the room to support more types of light emitting objects (for example, 'TubeLight', 'LEDLight', etc.),
# you would have to make many changes in the Room class. In this way, it violates the Dependency Inversion Principle.

from abc import ABC, abstractmethod

class Light(ABC):
    @abstractmethod
    def start(self):
        pass

class Lamp(Light):
    def start(self):
        return 'Lamp is On...'
class TubeLight(Light):
    def start(self):
        return 'TubeLight is On...'

class Room:
    def __init__(self, light):
        self.light = light

    def glow(self):
        return self.light.start()

rm = Room(Lamp())
print(rm.glow())
rm = Room(TubeLight())
print(rm.glow())