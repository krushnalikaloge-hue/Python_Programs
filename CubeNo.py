def Cube(No):
    Ans = No * No * No

    print("Cube is: ",Ans)

def main():
    Value = int(input("Enter the Number: "))

    Cube(Value)

if __name__=="__main__":
    main()