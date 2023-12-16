class Circle:
        def __init__(self,center,radius):
            self.center = center
            self.radius = radius
        def __str__(self):
            return f'Circle of center {self.center} and radius {self.radius}'
               
if __name__ == "__name__":
    c = Circle((150,100),75)
    print(c)

# python3 -c 'from circle import Circle; print(Circle((1,1),4))'