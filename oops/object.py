class MyNewClass:

    def __init__(self, x=0, y=0, **kwargs):
        self.x = x
        self.y = y
        print(f"init method executed after new. it is resp for initializing the newly created object and return void.\n {self.x}, {self.y}")

    def __new__(cls, *args, **kwargs):
        print(f"new method executed first. it is resp for creating the instance of class and return it \n{kwargs.items()}")
        return super().__new__(cls)

c = MyNewClass(2,5, name='python')
