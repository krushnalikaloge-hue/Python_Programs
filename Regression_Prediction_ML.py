# Write a python program using StandardScaler to perform feature scaling on the following dataset:
# [[25,20000], [30,40000], [35,80000]]
# Print he scaled dataset

import numpy as np
from sklearn.preprocessing import StandardScaler

def main():
    Data = np.array([
        [25,20000],
        [30,40000],
        [35,80000]
    ])

    Scaler = StandardScaler()

    ScaledData = Scaler.fit_transform(Data)

    print("Scaled Dataset: ")
    print(ScaledData)

if __name__=="__main__":
    main()