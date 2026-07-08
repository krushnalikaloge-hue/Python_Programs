import MarvellousNum

def ListPrime(Data):
    Sum = 0

    for NO in Data:
        if MarvellousNum.ChkPrime(No):
            Sum = Sum + No

    return Sum

def main():
    n = int(input("Number of Elements: "))

    list = []

    print("Enter the Elements: ")
    
    for i in range(n):
        Value = int(input())
        list.append(Value)

    Ret = ListPrime(list)

    print("Addition of prime numbers is: ",Ret)

if __name__=="__main__":
    main()