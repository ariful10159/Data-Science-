# problem 1
# Write a python program that takes a number as input and checks whether it is ever or odd

a = int(input("write any integer number: "))

if a%2==0:
    print(f"{a} is even number.")
else :
    print(f"{a} is odd number .")

# problem 02
# write a program that takes two numbers and an operator and performs the calculation

# b = int(input("Please input a number : "))
# c = int(input("input another a number : "))
# d = input("Please input a operator : ")

# if d=='+':
#    print(b+c)
# elif d =='-':
#    print(b-c)
# elif d== '*':
#     print(b*c)
# elif d=='/':
#     if c==0:
#         print("Invalid process")
#     else :
#         print(b/c)

# else:
#     print("write correct sign")







# problem 03
# write a program using a for loop that calculates the sum of even numbers between 1 and 100


a = range(1,100)
sum = 0
for i in a:
    if i % 2 == 0:
        sum = sum + i
    else:
        if (i>100):
            break
        else :
            continue
    i = i +2
    print("i = ", i )
    print("sum = ", sum)

print ("sum = ", sum)
