class Shape:
    def __init__(a):
        pass

    def area(a):
        return 0

class Square(Shape):
    def __init__(a, length):
        a.length = length

    def area(a):
        return a.length * a.length
shape = Shape()
square = Square(int(input())) 
print("Area of the shape:", shape.area())  
print("Area of the square:", square.area())  
