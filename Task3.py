# O1: Rectangle Class

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def display(self):
        print(f"Width: {self.width}")
        print(f"Height: {self.height}")


# Example usage
w = int(input("Enter width: "))
h = int(input("Enter height: "))

rect = Rectangle(w, h)
rect.display()
