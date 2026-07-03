def CountDigit(No):
    Count = 0

    while(No > 0):
        No = No // 10
        Count = Count + 1

    print("Count of Digit is: ",Count)

def main():
    Ret = int(input("Enter the Number: "))
    CountDigit(Ret)

if __name__=="__main__":
    main()
