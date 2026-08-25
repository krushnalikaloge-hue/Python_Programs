#Draw a boxplot for Attendance. Identify if any outliers are present.

import pandas as pd

import seaborn as sns

import matplotlib.pyplot as plt


Border = "-"*30

##################################################################################
# Boxplot Histogram of StudyHours
##################################################################################

print(Border)
print("Boxplot Histogram of StudyHours")
print(Border)

DataPath = "student_performance_ml.csv"

df = pd.read_csv(DataPath)

# BoxPlot

sns.boxplot(y="Attendance",data=df)

plt.title("Student performance case study")
plt.legend

plt.show()

# The boxplot shows the distribution of attendance. There are no visible outliers in the data. 

