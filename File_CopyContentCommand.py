import sys

def main():
    try:
        Source = open(sys.argv[1], "r")
        Destination = open("Demo.txt", "w")

        Data = Source.read()

        Destination.write(Data)

        print("Contents copied successfully")

        Source.close()
        Destination.close()

    except FileNotFoundError:
        print("File is not found")

if __name__ == "__main__":
    main()