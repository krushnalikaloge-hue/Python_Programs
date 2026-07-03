def Prime(No):
    Count = 0

    for i in range(1, No + 1):
        if(No % i == 0):
            Count = Count + 1
    if(Count == 2):
        print("Prime Number")
    else:
        print("Not Prime Number")

def main():
    Ret = int(input("Enter the Number: "))
    Prime(Ret)

if __name__=="__main__":
    main()