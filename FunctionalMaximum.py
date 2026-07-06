Maximum = lambda No1, No2 : max(No1, No2)

def main():
    Value1 = int(input("Enter the first Number:"))
    Value2 = int(input("Enter the second Number: "))

    Ret = Maximum(Value1, Value2)

    print("Maximum number is: ",Ret)

if __name__=="__main__":
    main()