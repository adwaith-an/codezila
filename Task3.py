#Task 3
#O2: Calculate Area — Add a method getArea() that returns width × height.


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        print(f"Rectangle created with width: {self.width} and height: {self.height}")

    def getArea(self):
        return self.width * self.height

width = int(input("Enter the Width : "))
length = int(input("Enter the Length : "))

my_rectangle = Rectangle(width, length)

area = my_rectangle.getArea()

print(f"The area of the rectangle is: {area}") 
