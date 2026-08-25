# Display total no of student in the dataset
# count how many student are passed (FinalResult = 1)
# count how many student are failed (FinalResult = 0)

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

print("Total number of student in dataset: ")
print(len(df))

print("Count how many student passed (FinalResult = 1) ")
Count = (df["FinalResult"] == 1).sum()
print(Count)

print("Count how many student failed (FinalResult = 0) ")
Count = (df["FinalResult"] == 0).sum()
print(Count)


