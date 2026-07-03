def Perfect(No):
    Sum = 0

    for i in range(1, No):
        if(No % i == 0):
            Sum = Sum + i
        
    if(Sum == No):
            print("Perfect Number")
    else:
            print("Not Perfect Number")

def main():
    Value = int(input("Enter the Number: "))
    Perfect(Value)

if __name__=="__main__":
    main()
