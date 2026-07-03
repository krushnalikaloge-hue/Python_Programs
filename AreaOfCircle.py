def Circle(Radius):
    Ans = 3.14 * Radius * Radius
    print("Area of circle is: ",Ans)

def main():
    Radius = float(input("Enter the Radius: "))
    Circle(Radius)

if __name__=="__main__":
    main()