from multiprocessing import Pool

def Factorial(No):
    fact = 1
    for i in range(1, No + 1):
        fact = fact * i
    return fact

def main():
    Data = [10,15,20,25]

    p = Pool()
    ans = p.map(Factorial, Data)

    print(ans)

if __name__=="__main__":
    main()