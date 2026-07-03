def Reverse(No):
    Rev = " "

    for i in str(No):
        Rev = i + Rev

    print("Reverse is: ",Rev)

def main():
    Ret = int(input("Enter the Number: "))
    Reverse(Ret)

if __name__=="__main__":
    main()     
