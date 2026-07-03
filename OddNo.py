def Odd(No):
    print("Odd numbers are: ")

    for i in range(1, No + 1, 2):
        print(i, end=" ")

def main():
    Ret = int(input("Enter the number: "))
    Odd(Ret)

if __name__=="__main__":
    main()