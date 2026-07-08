#Accept No from the user and return addition of digits in that Number.
def SumDigits(No):
    sum = 0

    while(No > 0):
        digit = No % 10
        sum = sum + digit
        No = No // 10

    return sum

def main():
    Value = int(input("Enter the Number: "))

    Ret = SumDigits(Value)

    print("Sum of Digit is: ",Ret)

if __name__=="__main__":
    main()