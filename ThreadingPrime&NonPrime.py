import threading

def Prime(arr):
    print("Prime Numbers:")
    for no in arr:
        if no > 1:
            for i in range(2, no):
                if no % i == 0:
                    break
            else:
                print(no)

def NonPrime(arr):
    print("Non Prime Numbers:")
    for no in arr:
        if no <= 1:
            print(no)
        else:
            for i in range(2, no):
                if no % i == 0:
                    print(no)
                    break

def main():
    arr = list(map(int, input("Enter numbers: ").split()))

    t1 = threading.Thread(target=Prime, args=(arr,))
    t2 = threading.Thread(target=NonPrime, args=(arr,))

    t1.start()
    t1.join()

    t2.start()
    t2.join()

if __name__ == "__main__":
    main()