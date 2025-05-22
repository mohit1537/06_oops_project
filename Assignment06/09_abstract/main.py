from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self,widht,height):
        self.widht = widht
        self.height = height

    def area(self):
        return self.widht * self.height
if __name__ == "__main__":
    rect = Rectangle(2,8)
    print("Area of rectangle is: ", rect.area())