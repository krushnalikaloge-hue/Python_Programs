# Plot SleepHours against FinalResult.
# Does sleeping more guarantee success? Explain.

import pandas as pd

import matplotlib.pyplot as plt


Border = "-"*30

##################################################################################
# Scatterplot of SleepHours vs FinalResult
##################################################################################

print(Border)
print("Scatterplot of SleepHours vs FinalResult")
print(Border)

DataPath = "student_performance_ml.csv"

df = pd.read_csv(DataPath)

# Scatterplot

plt.scatter(
    df["SleepHours"],
    df["FinalResult"],
    label = "Students",
    alpha=0.8,
    marker='o',
    s=100,
    edgecolor="black",
    linewidth=1
)

plt.title("Student performance case study")
plt.xlabel("SleepHours")
plt.ylabel("Final Result")

plt.yticks([0,1])
plt.legend()
plt.show()

# From the graph, students with more sleep generally have better results, but sleep alone is not enough to guarantee.
# other factors such as study hours, attendance, and assignments can also affect success.

