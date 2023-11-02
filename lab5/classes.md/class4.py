import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def show(self):
        print(f"Coordinates: ({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self):
        dx = new_x - x
        dy = new_y - y
        distance = math.sqrt(dx**2 + dy**2)
        return distance

x = float(input("x-coordinate: "))
y = float(input("y-coordinate: "))
point = Point(x, y)

point.show()

new_x = float(input("new x-coordinate: "))
new_y = float(input("new y-coordinate: "))
point.move(new_x, new_y)
point.show()

distance = point.dist()
print(f"Distance between the two points: {distance}")
