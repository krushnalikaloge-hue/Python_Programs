# Create a plot showing realtionship between AssignmentsCompleted and FinalResult.
# Explain your observation

import pandas as pd

import matplotlib.pyplot as plt


Border = "-"*30

##################################################################################
# Scatterplot of AssignmentCompleted vs FinalResult
##################################################################################

print(Border)
print(" Scatterplot of AssignmentCompleted vs FinalResult")
print(Border)

DataPath = "student_performance_ml.csv"

df = pd.read_csv(DataPath)

# Scatterplot

plt.scatter(
    df["AssignmentsCompleted"],
    df["FinalResult"],
    label = "Students",
    alpha=0.8,
    marker='o',
    s=100,
    edgecolor="black",
    linewidth=1
)

plt.title("Student performance case study")
plt.xlabel("Assignment Completed")
plt.ylabel("Final Result")

plt.yticks([0,1])
plt.legend()
plt.show()

# From the above diagram,
# 1.Students who completed 2,3 and 4 assignments have FinalResult = 0 -> Fail.
# 2.Students who completed 5,6,7,8,and 9 assignments have FinalResult = 1 -> Pass.
# 3.We can observe that students completing 5 or more assignments passed, while those completing fewer assignments failed. 

