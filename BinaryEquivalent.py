def Binary(No):
    Ans = bin(No)

    print("Binary Equivalent is: ",Ans[2:])

def main():
    Value = int(input("Enter the Number: "))
    Binary(Value)

if __name__=="__main__":
    main()