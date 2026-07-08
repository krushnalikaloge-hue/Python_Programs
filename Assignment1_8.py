# Accept No from user and print that No of "*" on screen
def Display(No):
    for i in range(No):
        print("*")

def main():
    value = int(input("Enter the Number: "))

    Display(value)

if __name__=="__main__":
    main()