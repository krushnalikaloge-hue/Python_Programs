Minimum = lambda No1, No2 : min(No1, No2)

def main():
    Value1 = int(input("Enter the first Number:"))
    Value2 = int(input("Enter the second Number: "))

    Ret = Minimum(Value1, Value2)

    print("Minimum number is: ",Ret)

if __name__=="__main__":
    main()