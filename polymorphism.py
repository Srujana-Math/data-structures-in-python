class Box1:
    def __init__(self,name):
        self.name=name
    def printdetails(self):
        print("printing name: ",self.name)

class Box2(Box1):
    def __init__(self,name,roll):
        self.roll=roll
        Box1.__init__(self,name)

    def printdetails(self):
        print("Printing roll: ",self.roll)

b=Box2("Raj",35)
b.printdetails()
    

-->class Box1:
    def __init__(self,name):
        self.name=name
    def printdetails(self):
        print("printing name: ",self.name)

class Box2(Box1):
    def __init__(self,name,roll):
        self.roll=roll
        Box1.__init__(self,name)

    #def printdetails(self):
        #print("Printing roll: ",self.roll)

b=Box2("Raj",35)
b.printdetails()
