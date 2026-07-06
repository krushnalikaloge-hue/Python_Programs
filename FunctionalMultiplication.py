Mult = lambda No1, No2 : (No1 + No2)

def main():
    Value1 = int(input("Enter the first Number: "))
    Value2 = int(input("Enter the Second Number: "))

    Ret = Mult(Value1, Value2)

    print("Multiplication is: ",Ret)

if __name__=="__main__":
    main()
