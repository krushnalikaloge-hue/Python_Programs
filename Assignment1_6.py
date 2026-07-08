# Check No is Positive, Negative or Zero
def Check(No):
    if No > 0:
        print("Positive Number")
    elif No < 0:
        print("Negative Number")
    else:
        print("Zero")

def main():
    Value = int(input("Enter the Number: "))

    Check(Value)

if __name__=="__main__":
    main()
