#errors vs exception 

#compile time , run time 
# Error --> face problem compile time with syntax , indentation error 
# exception --> face run time which problem 

try:
    with open('rahim.txt','r') as f:
      print(f.read())
 #   print(10/0)
    print(10/10)
    a=[1,2,3]
    print(a[1])
    x = int("abc")
except ZeroDivisionError:
   print("Error : Division by zero is not possible")
except FileNotFoundError:
    print("File not found")
except ValueError:
    print("Invalid value")

#when try is execute then directly show else msg
else:
   print("Code executed successfully!!")
#finally part always execute
finally:
   print("Error does not matter , it must be run")

#Manually exception trigger
#make custom error
def check_file(filename):
   if not filename.endswith('.txt'):
      raise ValueError("only , Txt files are allowed")
      #program stoped here . because ValueError
   print("valid file")

check_file('data.csv')

#custom error handling
try:
   check_file('data.csv')
except Exception as e:
   print(e)