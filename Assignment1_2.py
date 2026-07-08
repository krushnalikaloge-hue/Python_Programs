# one Fun name as ChkNum() which accept one parameter. If No is even than it should display "Even No" o.w "Odd No" 
def ChkNum(No):
    if(No % 2 == 0):
        print("Even Number")
    else:
        print("Odd Number")

def main():
    Value = int(input("Enter the Number: "))

    ChkNum(Value)

if __name__=="__main__":
    main()
    