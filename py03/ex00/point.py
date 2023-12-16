class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

# POINT 1
str1 = input("Insert the coordinates of the first point: ")
x1= str1[0:str1.index(',')]
y1= str1[str1.index(',') + 1:]
p1 = Point(float(x1), float(y1))
# POINT 2
str2 = input("Insert the coordinates of the second point: ")
x2= str2[0:str2.index(',')]
y2= str2[str2.index(',') + 1:]
p2 = Point(float(x2), float(y2))

print("Their distance is: "),
print(((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)**(1/2))
