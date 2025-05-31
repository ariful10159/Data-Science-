# problem 03
# write a program using a for loop that calculates the sum of even numbers between 1 and 100

a = range(1,101)
sum = 0
for i in a:
    if i % 2 == 0:
        sum = sum + i
    else:
        if (i>101):
            break
        else :
            continue
    i = i +2
    # print("i = ", i )
    # print("sum = ", sum)

print ("sum = ", sum)
