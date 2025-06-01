class school :
    school_name = "Rampur high school"

    @staticmethod
    def calculate_grade(marks):
        if marks >=80:
            return 'A+'
        elif marks >=70:
            return 'A'
        else :
            return 'F'

print(school.calculate_grade(45))

# Python-এর static method মানে হচ্ছে এমন একটা 
# মেথড (function) যেটা ক্লাসের ভেতরে থাকে, কিন্তু 
# সেটা object বা class-এর কোন data ব্যবহার করে না।
    