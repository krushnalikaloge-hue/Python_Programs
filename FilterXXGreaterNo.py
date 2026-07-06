ChkLength = lambda Str : len(Str) > 5

def main():
    Data = ["Python","C","Marvellous","Java","ML"]

    print("Input Data is: ",Data)
    
    FData = list(filter(ChkLength,Data))

    print("Data after Filter: ",FData)

if __name__=="__main__":
    main()