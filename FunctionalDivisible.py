ChkDivisible = lambda No : (No % 5 == 0)

def main():
    Value = int(input("Enter the Number: "))

    Ret = ChkDivisible(Value)

    if(Ret == True):
        print("Number is Divisible by 5")
    else:
        print("Number is not Divisible by 5 ")

if __name__=="__main__":
    main()
