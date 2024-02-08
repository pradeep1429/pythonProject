from abc import ABC, abstractmethod

class AllInOnePrinter(ABC):
    @abstractmethod
    def print(self):
        pass

    @abstractmethod
    def scan(self):
        pass


class HPAllInOnePrinter(AllInOnePrinter):
    def print(self):
        return 'Printing...'

    def scan(self):
        return 'Scanning...'

class SimplePrinter(AllInOnePrinter):
    def print(self):
        return 'Printing...'

    def scan(self):
        pass

# 'SimplePrinter' is forced to have a 'scan' method, which violates the Interface Segregation Principle

class Printer(ABC):
    @abstractmethod
    def print(self):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan(self):
        pass

class AllInOnePrinter(Printer, Scanner):
    def print(self):
        return 'Printing...'

    def scan(self):
        return 'Scanning...'

class SimplePrinter(Printer):
    def print(self):
        return 'Printing...'