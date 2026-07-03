def Arithmatic(No1, No2):
    Add = No1 + No2
    Sub = No1 - No2
    Mult = No1 * No2
    Div = No1 / No2
    return Add, Sub, Mult, Div

def main():
    Value1 = int(input("Enter the first Number: "))
    Value2 = int(input("Enter the second Number: "))

    Ret1 , Ret2, Ret3, Ret4 = Arithmatic(Value1, Value2)

    print("Addition is: ",Ret1)
    print("Subtraction is: ",Ret2)
    print("Multiplication is: ",Ret3)
    print("Division is: ",Ret4)

if __name__=="__main__":
    main()