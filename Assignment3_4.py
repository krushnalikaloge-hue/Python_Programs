#Accept N Numbers from the user and store it into list.Accept one another No from user and return freq. of that No
def Frequency(Arr, No):
    Count = 0

    for i in Arr:
        if i == No:
            Count = Count + 1
        
    return Count

def main():
    Arr = []

    Num = int(input("Number of Elements: "))

    for i in range(Num):
        Arr.append(int(input()))

    No = int(input("Element to Search: "))

    print("Frequency is: ",Frequency(Arr, No))

if __name__=="__main__":
    main()