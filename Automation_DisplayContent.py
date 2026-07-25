#Write a program that reads and displays the contents of a specified text file every min.

import sys
import os
import time
import schedule

def DisplayContents(FileName):

    try:

        fobj = open(FileName, "r")

        Data = fobj.read()

        if(len(Data) == 0):
            print("File is empty")
        else:
            print("----------------------------------------")
            print(Data)
            print("----------------------------------------")

        fobj.close()

    except FileNotFoundError:
        print("Error : File not found")

    except PermissionError:
        print("Error : Permission denied")

    except Exception as obj:
        print("Error :", obj)

def main():

    Border = "-" * 40

    print(Border)
    print(" Marvellous Automation Script ")
    print(Border)

    if(len(sys.argv) == 2):

        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This automation script reads and displays the contents of a text file every minute.")
            print("For better usage please check --u flag")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Please execute the script as")
            print("python FileName.py FileName")

        else:

            DisplayContents(sys.argv[1])

            schedule.every(1).minutes.do(DisplayContents, sys.argv[1])

            while(True):
                schedule.run_pending()
                time.sleep(1)

    else:
        print("Invalid number of arguments")
        print("Please use --h or --u for more information")

    print(Border)
    print(" Thank you for using Marvellous Automation Script ")
    print(Border)

if __name__ == "__main__":
    main()