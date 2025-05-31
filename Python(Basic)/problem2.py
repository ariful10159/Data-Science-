# problem 02
# write a program that takes two numbers and an operator and performs the calculation

b = float(input("Please input a number : "))
c = input("Please input a operator : ")
d = float(input("input another a number : "))


if c =='+':
   print(b+d)
elif c =='-':
   print(b-d)
elif c== '*':
    print(b*d)
elif c=='/':
    if d==0:
        print("invalid")
    else :
        print(b/d)

else:
    print("write correct sign")
