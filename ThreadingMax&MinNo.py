import threading

def Maximum(arr):
    print("Maximum element is:", max(arr))

def Minimum(arr):
    print("Minimum element is:", min(arr))

def main():
    arr = list(map(int, input("Enter numbers: ").split()))

    t1 = threading.Thread(target=Maximum, args=(arr,))
    t2 = threading.Thread(target=Minimum, args=(arr,))

    t1.start()
    t1.join()

    t2.start()
    t2.join()

if __name__ == "__main__":
    main()