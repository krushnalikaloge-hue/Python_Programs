# Write a Python program that demonstrate how prediction change when K changes.
# Task: Predict the class of the same new point using K =1, K=3, K=5

import math

def EucDistance(P1, P2):
    Ans = math.sqrt((P1['X'] - P2['X'])**2 + (P1['Y'] - P2['Y'])**2)
    return Ans


def KNNClassifier(k):

    border = "-" * 30

    Data = [
        {'point':'A', 'X':1, 'Y':2, 'label':'Red'},
        {'point':'B', 'X':2, 'Y':3, 'label':'Red'},
        {'point':'C', 'X':3, 'Y':1, 'label':'Blue'},
        {'point':'D', 'X':5, 'Y':6, 'label':'Blue'}
    ]

    new_point = {'X':2, 'Y':2}

    print(border)
    print("KNN Classifier")
    print("K =", k)
    print(border)

    # Calculate distance
    for d in Data:
        d['distance'] = EucDistance(d, new_point)

    # Sort data
    sorted_data = sorted(Data, key=lambda item: item['distance'])

    print("Sorted Data")
    print(border)

    for d in sorted_data:
        print(d)

    print(border)

    # Select K nearest neighbours
    nearest = sorted_data[:k]

    print("Nearest", k, "members are:")
    print(border)

    for d in nearest:
        print(d)

    print(border)

    # Voting
    votes = {}

    for neighbours in nearest:
        label = neighbours['label']
        votes[label] = votes.get(label, 0) + 1

    print("Voting Result")
    print(border)

    for d in votes:
        print("Name :", d, "Number of votes :", votes[d])

    print(border)

    # Final Prediction
    iMax = 0
    Name = ""

    for d in votes:
        if votes[d] > iMax:
            iMax = votes[d]
            Name = d

    print("Final Prediction is :", Name)
    print(border)


def main():

    print("Prediction for K = 1")
    KNNClassifier(1)

    print("Prediction for K = 3")
    KNNClassifier(3)

    print("Prediction for K = 4")
    KNNClassifier(4)


if __name__ == "__main__":
    main()