# Drop the 'English' column from the original DataFrame.

import pandas as pd

data = {
    'Name' : ['Amit','Sagar','Pooja'],
    'Math' : [85,90,78],
    'Science' : [92,88,82],
    'English' : [75,85,82]
}

df = pd.DataFrame(data)
print(df)

df_dropped = df.drop(columns=['English'])
print(df_dropped)
