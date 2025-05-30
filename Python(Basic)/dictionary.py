# {}
# key value pair
# indexing er shujug ase 
# key gula immutable 

a= {'Rahim' : 12,'Karim': 14,'Fahim':78}

print(type(a))

for i in a:
    print(i)

print("==================")

for i in a.values():
    print(i)

print(a.keys(),a.values())   


for k,v in a.items():
    print(f"key values : {k}, values {v}")


b = [1,2,3]
c=["Mango","Banana","Apple"]

print(dict(zip(b,c)))


# dictionary comprehension
nums = list(range(0,11))

result= {i: "Even" if i%2 ==0 else "odd" for i in nums }
print ( result)