#filter(), map(), reduce()
from functools import reduce

ChkEven = lambda No : (No % 2 == 0)

Square = lambda No : (No * No)

Addition = lambda No1, No2 : (No1 + No2) 

def main():
    Data = [5,2,3,4,3,4,1,2,8,10]

    print("Input Data is: ",Data)

    FData = list(filter(ChkEven, Data))

    print("Data after Filter: ",FData)

    MData = list(map(Square, FData))

    print("Data after Map: ",MData)

    RData = reduce(Addition, MData)

    print("Data after Reduce: ",RData)

if __name__=="__main__":
    main()



