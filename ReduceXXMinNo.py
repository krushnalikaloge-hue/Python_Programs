from functools import reduce

MinNumber = lambda No1, No2 : No1 if No1 <  No2 else No2

def main():
    Data = [10,20,30,4,50]

    print("Input Data list: ",Data)

    Ret = reduce(MinNumber,Data)

    print("Minimum number is:  ",Ret)

if __name__=="__main__":
    main()