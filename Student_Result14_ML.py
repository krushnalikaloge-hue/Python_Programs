# plot a pie chart of subject marks for 'Bob'

import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Name' : ['Amit','Bob','Pooja'],
    'Math' : [85,90,78],
    'Science' : [92,88,82],
    'English' : [75,85,82],
    'Gender' : ['Male','Male','Female']
}

df = pd.DataFrame(data)

bob = df[df['Name']=='Bob'][['Math','Science','English']].values.flatten()
labels = ['Math','Science','English']

plt.pie(bob,labels = labels, autopct = '%1.1f%%')
plt.title("Bob's Subject Wise Distribution")
plt.show()
