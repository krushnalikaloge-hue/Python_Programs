# Write a python program to calculate the Euclidean distance between two points before and after applying feature scaling 
# and explain the differnce in results.

import numpy as np
from sklearn.preprocessing import StandardScaler

def main():
    Point1 = np.array([25, 200000])
    Point2 = np.array([35,800000])

    # Euclidean distance before scaling
    DistanceBefore = np.linalg.norm(Point1 - Point2)

    # Dataset for scaling

    Data = np.array([
        [25, 200000],
        [30,400000],
        [35,800000]
    ])

    Scaler = StandardScaler()
    ScaledData = Scaler.fit_transform(Data)

    # Scaled points
    ScaledPoint1 = ScaledData[0]
    ScaledPoint2 = ScaledData[2]

    # Euclidean distance after scaling
    DistanceAfter = np.linalg.norm(ScaledPoint1 - ScaledPoint2)

    print("Distance before scaling =",DistanceBefore)
    print("Distance after scaling =",DistanceAfter)

if __name__=="__main__":
    main()