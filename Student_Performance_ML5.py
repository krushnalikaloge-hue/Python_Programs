# Based on the dataset values, analyze whether:
#     Higher StudtHours increase the chance of passing.
#     Higher Attendance imporoves FinalResult. write the your obervation

import pandas as pd

Border = "-"*30

##################################################################################
# StudyHours vs Chance of Passing
##################################################################################

print(Border)
print("Student_performance")
print(Border)

DataPath = "student_performance_ml.csv"

df = pd.read_csv(DataPath)

PassData = df[df["FinalResult"]==1]
Number_PassStudents = len(PassData)
print("Number of pass students: ",Number_PassStudents)

Studyhrs_Pass = PassData["StudyHours"].sum()
print("Study Hours of Pass Students: ",Studyhrs_Pass)

Average_StudyHrs_Pass = Studyhrs_Pass/Number_PassStudents
print("Average of Study Hours of Pass students:",Average_StudyHrs_Pass)

print(Border)

FailData = df[df["FinalResult"]==0]
Number_FailStudents = len(FailData)
print("Number of Fail Students: ",Number_FailStudents)

Studyhrs_Fail = FailData["StudyHours"].sum()
print("Study Hours of Fail Students: ",Studyhrs_Fail)

Average_StudyHrs_Fail = Studyhrs_Fail/Number_FailStudents
print("Average of study Hours of Fail Students: ",Average_StudyHrs_Fail)

print(Border)

print("Higher StudyHours increase the change of passing is proved ")

print(Border)

Border = "-"*30

#Pass students have higher study hours than failed students.so it conclude that higher studyhrs may increase the chance of passing.

#############################################################################################################
# Attendance improves Final Result
#####################################################################################################

print(Border)
print("Attendance improves Final Result")
print(Border)

PassData = df[df["FinalResult"]==1]
Number_PassStudents = len(PassData)
print("Number of Pass Students: ",Number_PassStudents)

Attendance_Pass = PassData["Attendance"].sum()
print("Attendance of Pass Students: ",Attendance_Pass)

Average_Attendance_Pass = Attendance_Pass/Number_PassStudents
print("Average Attendance of pass Students: ",Average_Attendance_Pass)

print(Border)

FailData = df[df["FinalResult"]==0]
Number_FailStudents = len(FailData)
print("Number of Fail Students: ",Number_FailStudents)

Attendance_Fail = FailData["Attendance"].sum()
print("Attendance of Fail Students: ",Attendance_Fail)

Average_Attendance_Fail = Attendance_Fail/Number_FailStudents
print("Average Attendance of Fail Students: ",Average_Attendance_Fail)

print(Border)









