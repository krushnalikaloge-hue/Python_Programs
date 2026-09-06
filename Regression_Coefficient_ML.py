# Write the python program that calculate the variance and standard deviation of the dataset:
# [6,7,8,9,10,11,12]
# Display Both Result

import numpy as np

def main():
    Data = np.array([6,7,8,9,10,11,12])

    Variance = np.var(Data)
    StandardDeviation = np.std(Data)

    print("Variance =",Variance)
    print("Standard Deviation =",StandardDeviation)

if __name__=="__main__":
    main()
