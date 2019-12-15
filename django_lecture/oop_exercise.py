class Circle():

    #class object attribute
    PI=3.14

    def __init__(self,radius=1):
        self.radius=radius

    def area(self):
        return self.radius*self.radius*Circle.PI


myc=Circle(3)
print(myc.area())
