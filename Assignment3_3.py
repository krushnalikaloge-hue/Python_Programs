#Accept N Numbers from the user and store it into list. Return minimum No from the list.
def Minimum(list):
    Min = list[0]

    for i in list:
        if i < Min:
            Min = i

    return Min

def main():
    Arr = []

    Value = int(input("Enter the Number of elements: "))

    for i in range(Value):
        Arr.append(int(input()))

    print("Minimum number is: ",Minimum(Arr))

if __name__=="__main__":
    main()
    