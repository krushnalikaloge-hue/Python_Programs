def main():
    try:
        fobj = open("Demo.txt","r")
        print("file gets opened")

        Data = fobj.read()

        print(Data)

        fobj.close()

    except FileNotFoundError:
        print("File is not found in current directory")

if __name__=="__main__":
    main()
