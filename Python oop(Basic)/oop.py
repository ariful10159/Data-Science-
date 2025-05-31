#create a class , it named car.this class inner make object
#Brand , model 

#_init_() : Dunder method , constructor
# constructor 3 types
# Default constructor
# Parameterized constructor 
# Default Value constructor

# function and method 
#nomally amra jake function boli, seta ke class er 
# modde banale amra atake method boli 

#=================================
#method 1
#---------------------------
# class car:
#     def _init_(self):
#         self.brand =""
#         self.model= ""
    

# car1 = car()
# car1.brand = "Toyota"
# car1.model = "Corolla"
# print(car1.brand)
# print(car1.model)

# car2 = car()
# car2.brand = "Honda"
# car2.model = "CDI"
# print(car2.brand, car2.model)

#==========================
#method 02
#--------------------------

# class car :
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model

# car1 = car("toyota","Corolla")   
# print(car1.brand)
# print(car1.model) 

# car2 = car("Honda","Civic")
# print(car2.brand)
# print(car2.model)

#==========================
#method 3 
#by default amra bole dei 
#--------------------------

class car:
    def __init__(self,brand = "Honda", model="civic"):
        self.brand= brand
        self.model = model 

car1 = car()
print(car1.brand, car1.model) 
        


