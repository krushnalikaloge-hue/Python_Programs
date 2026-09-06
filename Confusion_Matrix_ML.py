# write a python program that calculates TP, TN, FP, FN for the following arrays:
# actual = [1,1,1,1,0,0,0,0]
# predicted = [1,1,0,1,0,1,0,0]
# Display all four values

from sklearn.metrics import confusion_matrix

def main():
    actual = [1,1,1,1,0,0,0,0]
    predicted = [1,1,0,1,0,1,0,0]

    TN, FP, FN, TP = confusion_matrix(actual,predicted).ravel()

    print("True Positive (TP) =", TP)
    print("True Negative (TN) =", TN)
    print("False Positive (FP) =",FP)
    print("False Neagative (FN) =",FN)

if __name__=="__main__":
    main()