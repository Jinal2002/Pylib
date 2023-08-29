# Area of Triangle

class Area:
    def _init_(self,b,h):
        
        self.b = float(b)
        self.c = float(h)

b= int(input("b="))
h= int(input("h="))

class triangle(Area):
    def area(self):
        s = 0.5* b*h
        return s      

t = triangle()
# print("area : {}".format(t.area()))
print("araa", t.area())