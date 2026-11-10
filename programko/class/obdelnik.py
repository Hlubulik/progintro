class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height 
    def area(self):
        x = self.width
        h = self.height
        area = x * h
        return(area)
    def perimeter(self):
        x = self.width
        h = self.height
        perimeter = 2 * (x + h)
        return(perimeter)
    def describe(self):
        if self.width != self.height:
            print(f"Je to obdelnik {self.width}x{self.height}, obsah {self.area()}")

        elif self.width == self.height:
            print(f"Je to ctverec {self.width}x{self.height}, obsah {self.area()}")
    # def is_square(self):


a = Rectangle(2, 3)
print(a.area())
print(a.perimeter())
print(a.describe())
# scale(3)