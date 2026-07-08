def CountDigit(No):
    count = 0

    while(No > 0):
        No = No // 10
        count = count + 1

    return count

def main():
    Value = int(input("Enter the Number: "))
    Ret = CountDigit(Value)
  
    print("Number of Digit: ",Ret)

if __name__=="__main__":
    main()