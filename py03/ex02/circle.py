import sys

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Circle:
        def __init__(self,center,radius):
            self.center = Point(*center)
            self.radius = radius
        def contains(self, point):
            return ((self.center.x - point.x) ** 2 + (self.center.y - point.y) ** 2)**(1/2) <= self.radius


if __name__ == "__main__":
    if len(sys.argv) != 3 :
        print("Error! Insert 3 args!")
    else:
        p1 = Point(float(0), float(0))
        p2 = Point(float(sys.argv[1]), float(sys.argv[2]))
        if ((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)**(1/2) <= 1:
            print(f'The Point ({sys.argv[1]}, {sys.argv[2]}) lies in the circle of center (0, 0) and radius 1')
        else:
            print(f'The Point ({sys.argv[1]}, {sys.argv[2]}) lies out the circle of center (0, 0) and radius 1')


# python3 -c 'from circle import Circle,Point; print(Circle((0,0),2).contains(Point(1,1)))'