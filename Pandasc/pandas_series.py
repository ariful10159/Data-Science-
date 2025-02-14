import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)

#label 
print(myvar[0])

# create own Labels 

myvar1 = pd.Series(a, index=["x","y","z"])
print(myvar1)

print(myvar1["z"])


calories = {"day1": 420, "day2": 380, "day3": 390}

myvar2 = pd.Series(calories)

print(myvar2)


data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

myvar3 = pd.DataFrame(data)

print(myvar3)