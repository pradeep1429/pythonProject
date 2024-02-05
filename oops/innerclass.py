
class student:
    def __init__(self, name, num, lap):
        self.name = name
        self.num = num
        self.lap = lap

    def show(self):
        print(self.name, self.num)
        self.lap.show()

    class laptop:
        def __init__(self, cpu, ram):
            self.cpu = cpu
            self.ram = ram

        def show(self):
            print(self.cpu, self.ram)

lap = student.laptop("i3", 16)
s1 = student("python", "29", lap)
s1.show()