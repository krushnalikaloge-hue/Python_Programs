def main():
    try:
        fobj = open("Demo.txt","r")
        print("file gets opened")

        Count = 0

        for line in fobj:
            Count = Count + 1

        print("Total number of lines is: ",Count)

        fobj.close()

    except FileNotFoundError:
        print("file is not found in current directory")

if __name__=="__main__":
    main()

        