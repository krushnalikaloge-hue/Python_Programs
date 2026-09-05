# Implement simple linear regression manually without using any ML library.
# Dataset  X = [1,2,3,4,5]  Y = [3,4,2,4,5]
# Tasks -> calculate 1) Mean of X(X bar)      2) Mean of Y(Y bar)
#                    3) Slope(m)              4) Intercept(c)

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

def Predictor():

    # Load the Data
    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]

    print("Values of independant variables X : ",X)
    print("Values of dependant variables Y : ",Y)

    # Calculate sum of X and Y
    sum_x = 0
    sum_y = 0

    for i in range(len(X)):
        sum_x = sum_x + X[i]
        sum_y = sum_y + Y[i]

    # Calculate Mean
    # Formula : Xbar = sum(X) / n
    #           Ybar = sum(Y) / n

    mean_x = sum_x / len(X)
    mean_y = sum_y / len(Y)

    print("Mean_X is : ",mean_x)
    print("Mean_Y is : ",mean_y)

    n = len(X)

    numerator = 0
    denominator = 0

    # Calculate slope m
    # formula: m = Sum((X-xbar) * (Y-ybar)) / Sum((X-xbar) ** 2)
    for i in range(n):
        numerator = numerator + ((X[i] - mean_x) * (Y[i] - mean_y))
        denominator = denominator + ((X[i] - mean_x)**2)

    # Calculate slope
    m = numerator / denominator

    print("Slope of line is ie m : ",m)

    # calculate Y intercept
    # formula: Y = mX + c
    #          c = Ybar - m*Xbar
    c = mean_y - m * mean_x

    print("Y intercept ie C : ",c)

    # Regression Equation Formula: Y = mX + c
    print("Regression equation: Y=",m,"X +",c)

    # Predict Y for x = 6
    # formula : Y = mx + c

    x = 6
    predicted_y = m * x + c
    print("Predicted Y for X = 6 : ",predicted_y)

def main():
    Predictor()

if __name__=="__main__":
    main()

