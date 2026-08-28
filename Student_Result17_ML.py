# Export the final DataFrame to a CSV file 

import pandas as pd

data = {
    'Name' : ['Amit','Sagar','Pooja'],
    'Math' : [85,90,78],
    'Science' : [92,88,82],
    'English' : [75,85,82],
    'Gender' : ['Male','Male','Female']
}

df = pd.DataFrame(data)
print(df)

df['Total'] = df['Math'] + df['Science'] + df['English'] 

df['Status'] = df['Total'].apply(lambda x: 'Pass' if x >= 250 else 'Fail')

df.to_csv("student_result.csv",index=False)

print("DataFrame exported to csv successfully")
