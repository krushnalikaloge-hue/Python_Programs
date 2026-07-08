import threading

def Small(Str):
    Count = 0

    for ch in Str:
        if(ch >= 'a' and ch <= 'z'):
            Count = Count + 1

    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    print("Lowercase Count :", Count)


def Capital(Str):
    Count = 0

    for ch in Str:
        if(ch >= 'A' and ch <= 'Z'):
            Count = Count + 1

    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    print("Uppercase Count :", Count)


def Digits(Str):
    Count = 0

    for ch in Str:
        if(ch >= '0' and ch <= '9'):
            Count = Count + 1

    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    print("Digit Count :", Count)


def main():

    Value = input("Enter String : ")

    t1 = threading.Thread(target=Small, args=(Value,), name="Small")
    t2 = threading.Thread(target=Capital, args=(Value,), name="Capital")
    t3 = threading.Thread(target=Digits, args=(Value,), name="Digits")

    t1.start()
    t1.join()

    t2.start()
    t2.join()

    t3.start()
    t3.join()

if __name__ == "__main__":
    main()