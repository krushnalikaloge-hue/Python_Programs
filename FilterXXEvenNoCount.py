ChkEven = lambda No : (No % 2 == 0)

def main():
    Data = [2,5,4,11,16,20,35]

    print("Input Data is: ",Data)

    FData = list(filter(ChkEven,Data))

    print("Count of even numbers: ",len(FData))

if __name__=="__main__":
    main()