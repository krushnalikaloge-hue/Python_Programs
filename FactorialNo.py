def Factorial(No):
    Ans = 1
    
    for i in range(1, No + 1):
        Ans = Ans * i

    print("Factorial is: ",Ans)

def main():
    Ret = int(input("Enter the Number: "))
    Factorial(Ret)

if __name__=="__main__":
    main()