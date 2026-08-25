# Use value_counts() to analyze the distribution of FinalResult.
# Calulate the percentage og Pass and fail student.
# Is the dataset balanced ? Justify your answer.

import pandas as pd

Border = "-"*30

##################################################################################
# Student_Performance
##################################################################################

print(Border)
print("Student_performance")
print(Border)

DataPath = "student_performance_ml.csv"

df = pd.read_csv(DataPath)

print("Distribution of FinalResult: ")

DistributionOfResult = df["FinalResult"].value_counts()
print("Distribution Result is: ",DistributionOfResult)

NumberofStudents = len(df)
print("Total Students are: ",NumberofStudents)

PassStudents = (df["FinalResult"] == 1).sum()
Percentage_PassStudents = (PassStudents/NumberofStudents) * 100
print("Percentage of pass students: ",Percentage_PassStudents)

FailStudents = (df["FinalResult"] == 0).sum()
Percentage_FailStudents = (FailStudents/NumberofStudents) * 100
print("Percentage of fail students: ",Percentage_FailStudents)


#PassStudent = 60% and FailStudents = 40%
#Dataset is not perfectly balanced but it is not highly imbalanced either



