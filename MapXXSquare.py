Square = lambda No : (No * No)

def main():
    Data = [2,4,6,8,10]

    print("Input data is: ",Data)

    MData = list(map(Square,Data))

    print("Data after Map: ",MData)

if __name__=="__main__":
    main()