#filter(), map(), reduce()
from functools import reduce

ChkNo = lambda No : (No >= 70 and No <= 90)

Increment = lambda No : (No + 10)

Multiplication = lambda No1, No2 : (No1 * No2)

def main():
    Data = [4,34,36,76,68,24,89,23,86,90,45,70]

    print("Input Data is: ",Data)

    FData = list(filter(ChkNo, Data))

    print("Data after Filter: ",FData)

    MData = list(map(Increment, FData))

    print("Data after Map: ",MData)

    RData = reduce(Multiplication, MData)

    print("Data after Reduce: ",RData)

if __name__=="__main__":
    main()



