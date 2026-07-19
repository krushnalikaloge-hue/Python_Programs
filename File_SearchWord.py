def main():
    try:
        fobj = open("Demo.txt","r")
        print("file gets opened")

        Data = fobj.read()

        Word = input("Enter the word to be search: ")

        if Word in Data:
            print("Word found")
        else:
            print("Word is not found")

        fobj.close()

    except FileNotFoundError:
        print("File is not found in current directory")

if __name__=="__main__":
    main()