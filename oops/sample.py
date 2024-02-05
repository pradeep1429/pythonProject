
class Computer:
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("config is: {} cpu {}GB ram".format( self.cpu, self.ram))

comp1 = Computer("i3",8)
comp2 = Computer("i5",16)
comp1.config()
comp2.config()
