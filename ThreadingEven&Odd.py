import time
import threading

def Even(No):
    print("Even Number: ")

    for i in range(2,21,2):
        print(i)

def Odd(No):
    print("Odd Number: ")

    for i in range(1,20,2):
        print(i)

def main():

    start_time = time.perf_counter()

    t1 = threading.Thread(target=Even, args=(100000,))
    t2 = threading.Thread(target=Odd, args=(100000,))

    t1.start()
    t1.join()

    t2.start()
    t2.join()
    
    end_time = time.perf_counter()
    
    print(f"Time Required is :{end_time - start_time:.4f}")



if __name__=="__main__":
    main()