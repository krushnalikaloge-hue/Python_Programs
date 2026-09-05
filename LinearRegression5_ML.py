# Using the same dadaset from above question calculate model performance .
# Tasks: 1) Predict all y values using regression equation 
#        2) Calculate: Mean Aquared Error(MSE) , R2 Score
# Show all intermediate  calculations

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def Predictor():

    # Load the data
    X = [1, 2, 3, 4, 5]
    Y = [3, 4, 2, 4, 5]

    print("Values of Independent variables X : ", X)
    print("Values of Dependent variables Y : ", Y)

    # Calculate sum of X and Y
    sum_x = 0
    sum_y = 0

    for i in range(len(X)):
        sum_x = sum_x + X[i]
        sum_y = sum_y + Y[i]

    # Calculate Mean of X and Y
    # Formula:
    # Xbar = Sum(X) / n
    # Ybar = Sum(Y) / n

    mean_x = sum_x / len(X)
    mean_y = sum_y / len(Y)

    print("Mean_X is : ", mean_x)
    print("Mean_Y is : ", mean_y)

    n = len(X)

    numerator = 0
    denominator = 0

    # Calculate slope m
    # Formula:
    # m = Sum((X-Xbar)*(Y-Ybar)) / Sum((X-Xbar)^2)

    for i in range(n):
        numerator = numerator + ((X[i] - mean_x) * (Y[i] - mean_y))
        denominator = denominator + ((X[i] - mean_x) ** 2)

    m = numerator / denominator

    print("Slope of line ie m : ", m)

    # Calculate Y intercept
    # Formula:
    # Y = mX + c
    # c = Ybar - m*Xbar

    c = mean_y - m * mean_x

    print("Y intercept ie C : ", c)

    # Predict all Y values
    # Formula:
    # Ypredicted = mX + c

    predicted_y = []

    for i in range(n):
        y = m * X[i] + c
        predicted_y.append(y)

    print("Predicted Y values : ", predicted_y)

    # Calculate Mean Squared Error
    # Formula:
    # MSE = Sum((Y-Ypredicted)^2) / n

    sum_error = 0

    for i in range(n):
        error = (Y[i] - predicted_y[i]) ** 2

        print("Squared Error for X =", X[i], ":", error)

        sum_error = sum_error + error

    mse = sum_error / n

    print("Sum of Squared Error : ", sum_error)
    print("Mean Squared Error : ", mse)

    # Calculate SS Total
    # Formula:
    # SS Total = Sum((Y-Ybar)^2)

    ss_total = 0

    for i in range(n):
        ss_total = ss_total + ((Y[i] - mean_y) ** 2)

    print("SS Total : ", ss_total)

    # Calculate SS Residual
    # Formula:
    # SS Residual = Sum((Y-Ypredicted)^2)

    ss_residual = 0

    for i in range(n):
        ss_residual = ss_residual + ((Y[i] - predicted_y[i]) ** 2)

    print("SS Residual : ", ss_residual)

    # Calculate R2 Score
    # Formula:
    # R2 = 1 - (SS Residual / SS Total)

    r2 = 1 - (ss_residual / ss_total)

    print("R2 Score : ", r2)

def main():
    Predictor()

if __name__ == "__main__":
    main()