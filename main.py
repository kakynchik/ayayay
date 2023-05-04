class circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
     print(f"радіус: {self.radius*self.radius*3.14}")
circle = circle(radius = 52)
circle.area()
