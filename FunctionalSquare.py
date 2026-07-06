Square = lambda No : (No * No)

def main():
    Value = int(input("Enter the Number: "))

    Ret = Square(Value)
    
    print("Square is: ",Ret)

if __name__=="__main__":
    main()