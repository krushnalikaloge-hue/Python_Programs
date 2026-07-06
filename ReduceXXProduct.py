from functools import reduce

Add = lambda No1, No2 : (No1 * No2)

def main():
    Data = [2,3,1,5,6]

    print("Input Data is: ",Data)

    RData = reduce(Add,Data)

    print("Data After Reduce:  ",RData)

if __name__=="__main__":
    main()