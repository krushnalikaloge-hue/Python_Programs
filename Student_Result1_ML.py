# Create a dataFrame for student marks and print basic information like shape, columns and data type.

import pandas as pd

data = {
    'Name' : ['Amit','Sagar','Pooja'],
    'Math' : [85,90,78],
    'Science' : [92,88,82],
    'English' : [75,85,82]
}

df = pd.DataFrame(data)

print("Shape: ",df.shape)
print("Columns: ",df.columns)
print("Data Types: \n",df.dtypes)