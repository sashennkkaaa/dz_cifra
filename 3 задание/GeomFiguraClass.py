class Geometry:
    def S(self):
        return 0

class Rectangle(Geometry):
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def S(self):
        return self.width * self.height

class Rhomb(Geometry):
    def __init__(self,d1,d2):
        self.d1 = d1
        self.d2 = d2

    def S(self):
        return 0.5 * self.d1 * self.d2
    
class Circle(Geometry):
    def __init__(self,R):
        self.R = R

    def S(self):
        return 3.14 * (self.R*self.R)

rec = Rectangle(5,5)
rhomb = Rhomb(5,2)
cir = Circle(5)
print ("Площадь прямоугольника: ", rec.S())
print ("Площадь ромба: ", rhomb.S())
print ("Площадь круга: ", cir.S())
