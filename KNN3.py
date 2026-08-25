# Use KNN to predict whether a student Passes or fails based on study hours and attendance
# Dataset             StudyHours    Attendance     Result
#                         2             60           Fail
#                         5             80           Pass
#                         1             85           Pass
#                         6             50           Fail

# Task : 1. Accept input from the user-  Study hours, Attendance percentage
#        2. Apply KNN alogrithm
#        3. Predict whether the student Passes or fails

import math

def EucDistance(P1, P2):
    Ans = math.sqrt((P1['StudyHours'] - P2['StudyHours'])**2 + (P1['Attendance'] - P2['Attendance'])**2)
    return Ans


def KNNClassifier(k = 3):

    border = "-" * 30

    Data = [
        {'StudyHours':2, 'Attendance':60, 'Result':'Fail'},
        {'StudyHours':5, 'Attendance':80, 'Result':'Pass'},
        {'StudyHours':6, 'Attendance':85, 'Result':'Pass'},
        {'StudyHours':1, 'Attendance':50, 'Result':'Fail'}
    ]

    print(border)
    print("Marvellous KNN Classifier")
    print(border)

    for d in Data:
        print(d)

    print(border)

    # Accept input from user
    StudyHours = int(input("Enter Study Hours: "))
    Attendance = int(input("Enter Attendance: "))

    new_point = {
        'StudyHours': StudyHours,
        'Attendance': Attendance
    }

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
        label = neighbours['Result']
        votes[label] = votes.get(label, 0) + 1

    print("Voting Result")
    print(border)

    for d in votes:
        print("Name :", d, "Number of votes :", votes[d])

    print(border)

    # Final prediction
    iMax = 0
    Name = ""

    for d in votes:
        if votes[d] > iMax:
            iMax = votes[d]
            Name = d

    print("Predicted Result:", Name)
    print(border)


def main():
    KNNClassifier(3)


if __name__ == "__main__":
    main()
         