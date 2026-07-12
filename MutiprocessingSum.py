from multiprocessing import Pool
import os

def Sum(No):
    Total = 0

    for i in range(1, No + 1):
        Total = Total + i

    print("Process ID :", os.getpid())
    print("Input Number :", No)
    print("Sum is :", Total)
    print()

def main():
    Data = [1000000, 2000000, 3000000, 4000000]

    p = Pool()

    p.map(Sum, Data)

    p.close()
    p.join()

if __name__ == "__main__":
    main()