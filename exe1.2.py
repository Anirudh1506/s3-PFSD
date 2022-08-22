import math
class Rect:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def peri(self):
        return 2*(self.a+self.b)
    def area(self):
        return self.a*self.b
class Circle:
    def __init__(self,r):
        self.r=r
    def peri(self):
        return 2*math.pi*self.r
    def area(self):
        return math.pi*self.r*self.r
class Triangle:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def peri(self):
        return self.a+self.b+self.c
    def area(self):
        s=(self.a+self.b+self.c)/2
        area=math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
        return area
r=Rect(5,6)
print(r.peri())
print(r.area())
c=Circle(10)
print(c.peri())
print(c.area())
t=Triangle(11,12,13)
print(t.peri())
print(t.area())
