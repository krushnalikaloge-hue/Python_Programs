#Create a Scatter of:
#StudyHours vs PreviousScore

import pandas as pd

import matplotlib.pyplot as plt
import seaborn

Border = "-"*30

##################################################################################
# Plot Histogram of StudyHours
##################################################################################

print(Border)
print("Plot Histogram of StudyHours")
print(Border)

DataPath = "student_performance_ml.csv"

df = pd.read_csv(DataPath)

PassData = df[df["FinalResult"] == 1]
FailData = df[df["FinalResult"] == 0]

#Scatter Plot

plt.scatter(
    PassData["StudyHours"],
    PassData["PreviousScore"],
    s = 100,
    marker = 'o',
    alpha = 0.8,
    edgecolor = "black",
    linewidths = 1,
    color= 'green',
    label='Pass'
)

plt.scatter(
    FailData["StudyHours"],
    FailData["PreviousScore"],
    s =100,
    marker = 'o',
    alpha = 0.8,
    edgecolor = 'black',
    linewidth = 1,
    color = 'red',
    label = 'Fail'
)

plt.title("Student performance case study")

plt.xlabel("Study Hours")
plt.ylabel("Previous Score")

plt.legend()
plt.grid()
plt.show()


