def Rectangle(Length, Width):

    Ans = Length * Width

    print("Area of Rectangle is: ",Ans)

def main():
    Length = float(input("Enter the Length: "))
    Width = float(input("Enter the Width: "))

    Rectangle(Length, Width)

if __name__=="__main__":
    main()