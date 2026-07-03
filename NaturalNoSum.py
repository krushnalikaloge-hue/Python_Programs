def Sum(No):
    Ans = 0
    for i in range(1, No + 1):
        Ans = Ans + i
        print("Sum is:", Ans)

def main():
    Ret = int(input("Enter the Number: "))
    Sum(Ret)

if __name__=="__main__":
    main()