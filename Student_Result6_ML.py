# Sort the DataFrame by 'Total' marks in descending order. 

import pandas as pd

data = {
    'Name' : ['Amit','Sagar','Pooja'],
    'Math' : [85,90,78],
    'Science' : [92,88,82],
    'English' : [75,85,82]
}

df = pd.DataFrame(data)

df['Total'] = df['Math'] + df['Science'] + df['English']
print(df)

df_sorted = df.sort_values(by='Total',ascending= False)
print(df_sorted)
