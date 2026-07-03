def Square(No):
    Ans = No * No
    
    print("Square no is: ",Ans)

def main():
    value = int(input("Enter the Number: "))
    
    Square(value)

if __name__=="__main__":
    main()