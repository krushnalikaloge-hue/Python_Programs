# Rename 'Math' column to 'Mathematics'

import pandas as pd

data = {
    'Name' : ['Amit','Sagar','Pooja'],
    'Math' : [85,90,78],
    'Science' : [92,88,82],
    'English' : [75,85,82]
}

df = pd.DataFrame(data)

df.rename(columns = {'Math':'Mathematics'},inplace= True)
print(df.head())


