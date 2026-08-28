# Display student who scored more than 85 in science.

import pandas as pd

data = {
    'Name' : ['Amit','Sagar','Pooja'],
    'Math' : [85,90,78],
    'Science' : [92,88,82],
    'English' : [75,85,82]
}

df = pd.DataFrame(data)

print(df[df['Science'] > 85])
