#Accept one No from the user and check whether No is Prime or not.
def Prime(No):
    Count = 0

    for i in range(1, No + 1):
        if(No % i == 0):
            Count = Count + 1
    if(Count == 2):
        print("It is Prime Number")
    else:
        print("It is Not Prime Number")

def main():
    Value = int(input("Enter the Number: "))
    Prime(Value)

if __name__=="__main__":
    main()