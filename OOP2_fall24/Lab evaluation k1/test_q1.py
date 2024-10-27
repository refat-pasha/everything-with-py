class Shape:
    def __init__(self,width,height):
        self.width = width
        self.height = height
class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def display(self):
        print(f"Rectangle : {self.width*self.height}")
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def display(self):
        pi = 3.1416
        print(f"Circle area : {pi * self.radius ** 2}")
r = Rectangle(5, 10)
c = Circle(7)
r.display()
c.display()


