def Palindrome(No):
    Temp = No
    Rev = 0

    while(No > 0):
        Digit = No % 10
        Rev = Rev * 10 + Digit
        No = No // 10

    if(Temp == Rev):
        print("Palindrome")
    else:
        print("Not Pailndrome ")

def main():
    Ret = int(input("Enter the Number: "))
    Palindrome(Ret)

if __name__=="__main__":
    main()