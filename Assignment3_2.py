#Accept N Numbers from the user and store it into list. Return maximum No from the list.
def Maximum(list):
    Max = list[0]

    for i in list:
        if i > Max:
            Max = i

    return Max

def main():
    Arr = []

    Value = int(input("Enter the Number of elements: "))

    for i in range(Value):
        Arr.append(int(input()))

    print("Maximum number is: ",Maximum(Arr))

if __name__=="__main__":
    main()
    