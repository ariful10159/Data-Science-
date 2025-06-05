class Father:
    def house(self):
        print("Father's house")

class Mother:
    def jewelry(self):
        print("Mother's jewelry")

class Child(Father, Mother):
    def bike(self):
        print("Child's bike")

# Create object
c = Child()
c.house()      # Inherited from Father
c.jewelry()    # Inherited from Mother
c.bike()       # Own method


# 📖 Bangla Explanation (বাংলায় ব্যাখ্যা):

# Multiple Inheritance মানে হচ্ছে – একটি ক্লাস একাধিক ক্লাস থেকে গুণাবলি (attribute) এবং মেথড (method) ইনহেরিট করে।

# 📚 উদাহরণ:

#     Child → Father এবং Mother দুই ক্লাস থেকেই ইনহেরিট করে।

#     ফলে Child ক্লাসে দুইটা parent এর মেথড ব্যবহার করা যায়।