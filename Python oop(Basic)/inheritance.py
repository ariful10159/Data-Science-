class grandfather: 
    def __init__(self, color, first_name):  # ঠিক করলাম
        self.color = color
        self.first_name = first_name


class father(grandfather):
    def __init__(self, hobby, color, first_name):  # ঠিক করলাম
        super().__init__(color, first_name)  # super call ঠিক আছে
        self.hobby = hobby

grand1 = grandfather("Red", "MD.")
fat = father("Cricket", "Green", "kazi")
print(fat.color)
