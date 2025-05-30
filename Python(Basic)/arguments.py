
#here , not define ami koto ta value nicci 
#just *args liklei amr sob value cole asbe 

def addition(*args):
    print(args)
    return sum(args)

r = addition(12,10,2,18,10)
print(r)


def my_func(f_name , l_name , age ):
    print(f"My name is {f_name} {l_name} . I am {age} years old")

my_func(22 , "Ariful" , "Islam")

my_func(age=22, f_name="Ariful" , l_name="Islam")

#Arbitary Number of key word arguments 

def my_function(**kwargs):
    print(kwargs)

my_function(age=22, f_name= "Ariful" , l_name= "Islam")



#default parameter and pass keyword 

def print_my_name(f_name, l_name= "Islam"):
    print(f_name, l_name)

print_my_name("Ariful") #Ariful islam(output)
print_my_name("Ariful", "Khan") #Ariful khan(output)


