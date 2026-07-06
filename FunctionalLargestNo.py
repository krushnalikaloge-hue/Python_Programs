Maximum = lambda No1, No2, No3: max(No1, No2, No3)

def main():
    Value1 = int(input("Enter the first Number:"))
    Value2 = int(input("Enter the second Number: "))
    Value3 = int(input("Enter the third Number: "))

    Ret = Maximum(Value1, Value2, Value3)

    print("Largest number is: ",Ret)

if __name__=="__main__":
    main()