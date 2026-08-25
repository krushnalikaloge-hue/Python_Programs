# Using pandas function calculate and display:
#   Average StudyHours
#   Average Attendance
#   Maximum PrevoiusScore
#   Minimum SleepHours

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

print("Average StudyHours: ")
TotalStudyHours = (df["StudyHours"].sum())
NumberOfStudents = len(df)
AverageStudyHours = (TotalStudyHours/NumberOfStudents)
print(AverageStudyHours)

print("Average Attendance: ")
TotalAttendance = (df["Attendance"].sum())
NumberOfStudents = len(df)
AverageAttendance = (TotalAttendance/NumberOfStudents)
print(AverageAttendance)

print("Maximum PreviousScore: ")
print(df["PreviousScore"].max())

print("Minimum SleepHours: ")
print(df["SleepHours"].min())


