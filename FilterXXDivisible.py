ChkDivisible = lambda No : (No % 3 == 0)and(No % 5 == 0)

def main():
    Data = [10,15,20,30,45,50,60,75]

    print("Input Data is: ",Data)
    
    FData = list(filter(ChkDivisible,Data))

    print("Data after Filter: ",FData)

if __name__=="__main__":
    main()