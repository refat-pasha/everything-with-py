class Shape: #parent class
    def __init__(self,dimention1, dimention2): #constructor
        self.dimention1 = dimention1
        self.dimention2 = dimention2
    def area(self):
        print("I am area method of shape class")
class triangle(Shape):
    def area(self):
        area = .5*(self.dimention1*self.dimention2)
        print(f"Area of triangle: {area}")
class rectangle(Shape):
    def area(self):
        area = (self.dimention1*self.dimention2)
        print(f"Area of rectangle: {area}")
t1 = triangle(20,30)
t1.area()
r1 = rectangle(20,30)
r1.area()