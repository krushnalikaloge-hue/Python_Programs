# Accept one Number from the user and return the Addition of its Factors
def SumFactors(No):
    sum = 0

    for i in range(1, No):
        if No % i == 0:
            sum = sum + i

    return sum

def main():
    Value = int(input("Enter the Number: "))
    Ret = SumFactors(Value)
    print("Addition of Factors is: ",Ret)

if __name__=="__main__":
    main()
