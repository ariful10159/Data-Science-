class shape:
    def area(self):
        print("Calculating area......")

class polygon(shape):
    def sides(self):
        print("Polygon has multiple sides")

class rectangle(polygon):
    def __init__(self,length, breath):
        self.length = length
        self.breath = breath
        
    def area(self):
        return self.length*self.breath
    
rec = rectangle(10 , 5)
rec.sides()
print(rec.area())
rec.area()