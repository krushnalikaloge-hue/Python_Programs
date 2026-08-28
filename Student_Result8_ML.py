# Plot a line chart of marks for 'Alice' across all subjects.

import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Name' : ['Alice','Sagar','Pooja'],
    'Math' : [85,90,78],
    'Science' : [92,88,82],
    'English' : [75,85,82]
}

df = pd.DataFrame(data)

alice_marks = df[df['Name'] == 'Alice'][['Math','Science','English']].values.flatten()
subjects = ['Math','Science','English']

plt.plot(subjects, alice_marks, marker='o')
plt.title("Alice's Marks")
plt.xlabel("Subject")
plt.ylabel("Marks")
plt.grid(True)
plt.show()
