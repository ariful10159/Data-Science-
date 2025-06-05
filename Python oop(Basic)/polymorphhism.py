# poly -> multiple 
# morphism -> form

# 1.Method overriding

class grandfather :
    def greet(self):
        print("Grandfather says")

class father(grandfather):
    def greet(self):
        print("Father says")

class children(father) :
    def greet(self):
        print("Children says")


gf = grandfather()
f = father()
c = children()

gf.greet()
f.greet()
c.greet()


# Method overloading

class shape :
    def area (self , a , b=10 ):
        return a*b
    
p = shape()
print(p.area(12))
print(p.area(12,10))