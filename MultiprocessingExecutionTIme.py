from multiprocessing import Pool
import time

def SumPower(No):
    Sum = 0

    for i in range(1, No + 1):
        Sum = Sum + (i ** 5)

    return Sum

def main():
    Data = [1000000, 2000000, 3000000, 4000000]

    start_time = time.perf_counter()
    p = Pool()
    Result = p.map(SumPower, Data)

    p.close()
    p.join()

    print(Result)

    end_time = time.perf_counter()

    print(f"Time required is: {end_time - start_time:.4f}")

if __name__=="__main__":
    main()