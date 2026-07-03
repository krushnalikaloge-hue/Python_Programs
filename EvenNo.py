def Even(No):
    print("Even Numbers are: ")

    for i in range(2, No + 1, 2):
        print(i, end=" ")

def main():
    Ret = int(input("Enter the Number: "))
    Even(Ret)

if __name__=="__main__":
    main()