import sys

def main():
    try:
        File1 = open(sys.argv[1], "r")
        File2 = open(sys.argv[2], "r")

        Data1 = File1.read()
        Data2 = File2.read()

        if Data1 == Data2:
            print("Success")
        else:
            print("Failure")

        File1.close()
        File2.close()

    except FileNotFoundError:
        print("File is not found")

if __name__ == "__main__":
    main()