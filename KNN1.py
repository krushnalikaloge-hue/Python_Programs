# Calculate Euclidean distance,   Sort distances,  Select K nearest neighbors,   Predict the class based on majority voting
# Datset       point     X    Y    Label
#                A       1    2     Red
#                B       2    3     Red
#                C       3    1     Blue
#                D       6    5     Blue

import math

def EucDistance(P1, P2):
    Ans = math.sqrt((P1['X'] - P2['X'])**2 + (P1['Y'] - P2['Y'])**2)
    return Ans

def KNNClassifier(k = 3):

    border = "-" * 50

    Data = [
        {'point':'A', 'X':1, 'Y':2, 'label':'Red'},
        {'point':'B', 'X':2, 'Y':3, 'label':'Red'},
        {'point':'C', 'X':3, 'Y':1, 'label':'Blue'},
        {'point':'D', 'X':5, 'Y':6, 'label':'Blue'}
    ]

    print(border)
    print("KNN Classifier")
    print(border)

    for d in Data:
        print(d)

    print(border)

    # Accept input
    x = int(input("Enter X coordinate : "))
    y = int(input("Enter Y coordinate : "))

    new_point = {'X':x, 'Y':y}

    print(border)
    print("Distances of all points")
    print(border)

    # Calculate distance
    for d in Data:
        d['distance'] = EucDistance(d, new_point)

    for d in Data:
        print(d)

    print(border)

    # Sort data
    sorted_data = sorted(Data, key = lambda item : item['distance'])

    print(border)
    print("Sorted Data")
    print(border)

    for d in sorted_data:
        print(d)

    print(border)

    # Select K nearest neighbours
    nearest = sorted_data[:k]

    print(border)
    print("Nearest", k, "members are :")
    print(border)

    for d in nearest:
        print(d)

    print(border)

    # Voting
    votes = {}

    for neighbours in nearest:
        label = neighbours['label']
        votes[label] = votes.get(label, 0) + 1

    print(border)
    print("Voting Result")
    print(border)

    for d in votes:
        print("Class :", d, " Votes :", votes[d])

    print(border)

    # Final Prediction
    iMax = 0
    Name = ""

    for d in votes:
        if(votes[d] > iMax):
            iMax = votes[d]
            Name = d

    print("Final Prediction is :", Name)
    print(border)

def main():
    KNNClassifier(3)

if __name__ == "__main__":
    main()  
    