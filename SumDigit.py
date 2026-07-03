def SumDigit(No):
    Sum = 0
    
    while(No > 0):
        Digit = No % 10
        Sum = Sum + Digit
        No = No // 10

    print("Sum of Digit is: ",Sum)

def main():
    Ret = int(input("Enter the Number: "))
    SumDigit(Ret)

if __name__=="__main__":
    main()
