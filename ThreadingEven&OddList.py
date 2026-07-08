import threading

def EvenList(Data):
    Sum = 0

    print("Even Elements :")

    for i in Data:
        if(i % 2 == 0):
            print(i)
            Sum = Sum + i

    print("Sum of Even Elements :", Sum)


def OddList(Data):
    Sum = 0

    print("Odd Elements :")

    for i in Data:
        if(i % 2 != 0):
            print(i)
            Sum = Sum + i

    print("Sum of Odd Elements :", Sum)


def main():
    Data = []

    Value = int(input("Enter number of elements : "))

    print("Enter the elements :")
    for i in range(Value):
        No = int(input())
        Data.append(No)

    t1 = threading.Thread(target=EvenList, args=(Data,))
    t2 = threading.Thread(target=OddList, args=(Data,))

    t1.start()
    t1.join()

    t2.start()
    t2.join()

if __name__ == "__main__":
    main()