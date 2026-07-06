ChkEven = lambda No : (No % 2 == 0)

def main():
    Data = [22,25,34,57,86,93]

    print("Input Data is: ",Data)

    FData = list(filter(ChkEven,Data))

    print("Data after Filter: ",FData)

if __name__=="__main__":
    main()