class A:
    def __init__(self):
        print("A")

class B(A):
    def __init__(self):
        super().__init__()
        print("B")

class C(B):
    def __init__(self):
        super().__init__()
        print("C")

obj = C() #A B C



# 1. `obj = C()` করলে `C` ক্লাসের `__init__()` কল হয়।
# 2. `C` ক্লাসের ভিতরে `super().__init__()` আছে, তাই এটি `B` ক্লাসের `__init__()` কল করে।
# 3. `B` এর `__init__()` এও `super().__init__()` আছে, তাই এটি `A` ক্লাসের `__init__()` কল করে।
# 4. প্রথমে `A` print হয় → তারপর `B` → তারপর `C`.

