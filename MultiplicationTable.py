def Table(No):
    for i in range(1,11):
        print(No * i)

def main():
    Value = int(input("Enter the Number: "))

    Table(Value)

if __name__=="__main__":
    main()