from multiprocessing import Pool

def PrimeCount(No):
    count = 0

    for i in range(2, No + 1):
        prime = True
        for j in range(2, i):
            if i % j == 0:
                prime = False
                break
            
        if prime:
            count = count + 1
    
    return count

def main():
    Data = [10000, 20000, 30000, 40000]
    p = Pool()
    Result = p.map(PrimeCount, Data)
    
    print(Result)

if __name__=="__main__":
    main()