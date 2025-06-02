#Association

class laptop:
    def __init__(self, brand , model):
        self.brand = brand
        self.model = model
        print(brand)

class student:
    def __init__(self, name, laptop_obj):
        self.name = name 
        self.laptop_v = laptop_obj

    def show_laptop_info(self):
        print(f"{self.name} has a laptop named {self.laptop_v.brand}, its model name {self.laptop_v.model}")

lp1 = laptop("Asus", "Eg")
student1 = student("Ariful", lp1) # main point 
student1.show_laptop_info()

#Aggregation : has a relationship 

class Department :
    def __init__(self, name):
        self.name = name 

class University:
    def __init__(self,name):
        self.name = name 
        self.departments = []
    def add_department(self,department):
        self.departments.append(department)
    
    def show_departments(self):
        return [Department.name for department in self.departments]
    
un1 = University("Abc")
dep1 = Department("programming")
dep2 = Department("Math")
un1.add_department(dep1)
un1.add_department(dep2)
print(un1.show_departments())




#composition 

# .
# .
# .
# .
# .



        
                
