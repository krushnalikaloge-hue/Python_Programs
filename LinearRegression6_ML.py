# Consider below task:
# 1. Train linear regression model.
# 2. Predict salary for ^ years of expercience.
# 3. Plot regression line using matplotlib
# Dataset        Expericence       salary
#                  1                20000
#                  2                25000
#                  3                30000
#                  4                35000
#                  5                40000

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def MarvellousPredictor():

    X = [1, 2, 3, 4, 5]
    Y = [20000, 25000, 30000, 35000, 40000]

    print("Values of Independent variables X : ", X)
    print("Values of Dependent variables Y : ", Y)

    sum_x = 0
    sum_y = 0

    for i in range(len(X)):
        sum_x = sum_x + X[i]
        sum_y = sum_y + Y[i]

    mean_x = sum_x / len(X)
    mean_y = sum_y / len(Y)

    print("Mean_X is : ", mean_x)
    print("Mean_Y is : ", mean_y)

    n = len(X)

    numerator = 0
    denominator = 0


    for i in range(n):
        numerator = numerator + ((X[i] - mean_x) * (Y[i] - mean_y))
        denominator = denominator + ((X[i] - mean_x) ** 2)

    m = numerator / denominator

    print("Slope of line ie m : ", m)

    c = mean_y - m * mean_x

    print("Y intercept ie C : ", c)

    print("Regression Equation : Y =", m, "X +", c)

    experience = 6
    predicted_salary = m * experience + c

    print("Predicted salary for 6 Years Experience : ",predicted_salary)

    x = np.linspace(1, 6, 10)

    y = c + m * x

    plt.plot(x, y, label="Regression Line")

    plt.scatter(X, Y, label="Data Points")

    plt.xlabel("X : Independent Variables")
    plt.ylabel("Y : Dependent Variables")

    plt.legend()

    plt.show()

def main():
    MarvellousPredictor()

if __name__ == "__main__":
    main()