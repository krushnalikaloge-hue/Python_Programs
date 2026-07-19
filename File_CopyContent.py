def main():
    try:
        Source = open("ABC.txt", "r")
        Destination = open("Demo.txt", "w")

        Data = Source.read()

        Destination.write(Data)

        print("Contents copied successfully")

        Source.close()
        Destination.close()

    except FileNotFoundError:
        print("File is not found in current directory")

if __name__ == "__main__":
    main()