# Add a new column 'Status' where students with total >= 250 are 'Pass' else 'Fail'

import pandas as pd

data = {
    'Name' : ['Amit','Bob','Pooja'],
    'Math' : [85,90,78],
    'Science' : [92,88,82],
    'English' : [75,85,82],
    'Gender' : ['Male','Male','Female']
}

df = pd.DataFrame(data)
print(df)

df['Total'] = df['Math'] + df['Science'] + df['English'] 

df['Status'] = df['Total'].apply(lambda x: 'Pass' if x >= 250 else 'Fail')
print(df[['Name','Total','Status']])
