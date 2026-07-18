class Demo:
    
    Value = 10

    def __init__(self, no1, no2):
        self.No1 = no1
        self.No2 = no2

    def Fun(self):
        print("Inside instance method Fun")
        print(self.No1)
        print(self.No2)

    def Gun(self):
        print("Inside instance method Gun")
        print(self.No1)
        print(self.No2)


Obj1 = Demo(11, 21)
Obj2 = Demo(51, 101)

Obj1.Fun()
Obj2.Fun()
Obj1.Gun()
Obj2.Gun()