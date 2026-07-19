def main():
    try:
        Name = input("Enter file name : ")
        Word = input("Enter word : ")

        fobj = open(Name, "r")

        Data = fobj.read()

        Count = Data.count(Word)

        print("Frequency is :", Count)

        fobj.close()

    except FileNotFoundError:
        print("File is not found")

if __name__ == "__main__":
    main()