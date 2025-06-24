import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'Numbers': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar) 

# checking pandas version 

print ( pd.__version__)