# Write the python program that calculates the mean of a dataset using NumPy for the following values:
# [6,7,8,9,10,11,12]

import numpy as np

def main():
    Data = np.array([6,7,8,9,10,11,12])

    Mean = np.mean(Data)

    print("Mean =",Mean)

if __name__=="__main__":
    main()