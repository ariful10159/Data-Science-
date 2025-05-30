import os
import pathlib
# file = open('name.txt','r')
# contact =  file.read()
# print(contact)
# file.close()


# with open('name.txt','r') as f:
#     contant = f.read()
#     print(contact)

# # with open ('name.txt','w') as f:
# #     f.write("Hello world\n")
# #     f.write ("i am writing in a file\n")

# with open('name.txt','a') as f:
#     f.write("i am a student in pstu")

# lines=['I love python\n','\nI am a new programmer\n']
# with open('name.txt','a') as f:
#     f.writelines(lines)
#file ase kih nah check korer jnno import os (import kora lagbe )
if os.path.exists('name.txt'):
    print("FIle.exists")
else:
    print("file not found")


file_path = pathlib.path('name.txt')
 
if file_path.exists():
    print("File exists")

print(os.path.abspath('name.txt')) #full location dibe
print(os.path.getsize('name.txt')) #bytes


with open('name.txt','r') as f:
    print(f.tell())#output coursor possition 

