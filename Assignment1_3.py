# Addition of two Numbers
def Add(No1, No2):
    Ans = No1 + No2
    return Ans
    

def main():
    Value1 = int(input("Enter the first number: "))
    Value2 = int(input("Enter the Second number: "))

    Ret = Add(Value1,Value2)

    print("Addition is: ",Ret)

if __name__=="__main__":
    main()