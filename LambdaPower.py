#Lambda Function to return power of two
Power = lambda No : (No ** 2)

def main():
    Value = int(input("Enter the Number: "))

    Ret = Power(Value)
    
    print("Power is: ",Ret)

if __name__=="__main__":
    main()