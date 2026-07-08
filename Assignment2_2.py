def Display(no):
    for i in range(no):
        for j in range(no):
            print("*", end ="\t")
        print()

def main():
    value = int(input("Enter the Number: "))

    Display(value)

if __name__=="__main__":
    main()