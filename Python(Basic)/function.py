# 2 types function
# user define function 
# Built in function 

mx = max([1,2,3,4,5])

print(f"Max value {mx} , {mx*3}")

#user define function 
#1,no input , no return 

def my_first_function():
    a = 10 
    b =12 
    print(a+b)

my_first_function() # called function 

def add_two_number(a,b): # argument
    print(a+b)

add_two_number(5,10)    #here 5, 10 is parameter 


#2.input, return

def multiple_two_number(a,b):
    return a*b

result = multiple_two_number(12,3)
print(result)

#no input , return
def hello():
    return "Hello"

greetings = hello()
print(greetings)



 
