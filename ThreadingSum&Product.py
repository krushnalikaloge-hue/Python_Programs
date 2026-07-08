import threading

def Sum(arr):
    print("Sum =", sum(arr))

def Product(arr):
    p = 1
    for i in arr:
        p = p * i
    print("Product =", p)

def main():
    arr = list(map(int, input("Enter numbers: ").split()))

    t1 = threading.Thread(target=Sum, args=(arr,))
    t2 = threading.Thread(target=Product, args=(arr,))

    t1.start()
    t1.join()

    t2.start()
    t2.join()

if __name__ == "__main__":
    main()