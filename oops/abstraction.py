from abc import abstractmethod, ABC

class Computer(ABC):
    @abstractmethod
    def status(self):
        pass

class laptop(Computer):
    def status(self):
        print("running")
    def type(self):
        print("WIndows")

com = laptop()
com.status()
com.type()