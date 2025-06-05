class Father:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print("Father's Name:", self.name)

class Son(Father):  # Single Inheritance
    def show_son(self):
        print("I am the son.")

# Object create
s = Son("Mr. Rahim")
s.show_name()   # Inherited from Father
s.show_son()    # Own method
