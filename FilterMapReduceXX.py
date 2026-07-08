from functools import reduce

def CheckPrime(No):
    if No < 2:
        return False

    for i in range(2, No):
        if(No % i == 0):
            return False

    return True

def Multiply(No):
    return No * 2

def Maximum(No1, No2):
    if(No1 > No2):
        return No1
    else:
        return No2

def main():

    Data = [2,70,11,10,17,23,31,77]

    print("Input Data is: ",Data)

    FData = list(filter(CheckPrime, Data))
    print("Data after filter :", FData)

    MData = list(map(Multiply, FData))
    print("Data after map :", MData)

    RData = reduce(Maximum, MData)
    print("Data after reduce :", RData)

if __name__ == "__main__":
    main()