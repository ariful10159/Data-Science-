#anonymous function --> unnamed
import functools
def square(x):
    return(x*x)

print(square(5))


#lamda arguments : expression 

square1 = lambda x : x*x
print(square1(4))

add =lambda a,b : a+b
print(add(3,4))


#==============================
students = [('Rahim',50),('Karim',26),('Ariful',32)]

sorted_students = sorted(students , key = lambda x : x[1])
print(sorted_students)

#-------------------------------------
#map(), filter(), reduce()

#map

nums = [1,2,3,4]
sq_nums = list(map(float, nums))
# one by one korty hoy , a jnno lambda use koresi 
sq_nums1 = list(map(lambda x : x*x, nums))
print(sq_nums1)
print(sq_nums)


#filter 
even = list(filter(lambda x : x%2==0, nums))
print(even)

#Reduce 
sum = functools.reduce(lambda x,y : x+y , nums)
print(sum)