# Load the file student_performance_ml.csv using pandas
# Display :
# first 5 records, last 5 records, total no of rows & coln
# list of coln names, Data Type of each coln 

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

print("First 5 records are: ")
print(df.head(5))

print("Last 5 records are: ")
print(df.tail(5))

print("total no of rows and columns: ")
print(df.shape)

print("List of columns names: ")
print(list(df.columns))

print("List of Column names: ")
print(list(df.dtypes))
