# Accept N Numbers from the user and store it into list. Return addition of all element from the list.
def Addition(Data):
    Sum = 0

    for No in Data:
        Sum = Sum + No

    return Sum

def main():
    Arr = []

    Size = int(input("Enter the Number of elements: "))

    print("Enter the elements: ")
    for i in range(Size):
        Value = int(input())
        Arr.append(Value)

    Ans = Addition(Arr)

    print("Addition is: ",Ans)

if __name__=="__main__":
    main()
    