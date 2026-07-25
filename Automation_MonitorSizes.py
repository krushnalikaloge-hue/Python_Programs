#Write a python program that monitors the size of a specified file every 30 sec.

import sys
import os
import time
import datetime
import schedule

def FileMonitor(FilePath):

    if(os.path.exists(FilePath) == False):
        print("File does not exist")
        return

    Size = os.path.getsize(FilePath)

    fobj = open("FileSizeLog.txt","a")

    fobj.write("File Path : " + FilePath + "\n")
    fobj.write("File Size : " + str(Size) + " Bytes\n")
    fobj.write("Date and Time : " + datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p") + "\n")
    fobj.write("----------------------------------------\n")

    fobj.close()

    print("File Path :", FilePath)
    print("File Size :", Size, "Bytes")
    print("Information stored in FileSizeLog.txt")
    print("----------------------------------------")

def main():

    Border = "-" * 40

    print(Border)
    print(" Marvellous Automation Script ")
    print(Border)

    if(len(sys.argv) == 2):

        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This automation script monitors the size of a file every 30 seconds.")
            print("For better usage please check --u flag")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Please execute the script as")
            print("python FileName.py FilePath")
            print("FilePath should be absolute path")

        else:

            if(os.path.exists(sys.argv[1]) == False):
                print("File does not exist")
                return

            FileMonitor(sys.argv[1])

            schedule.every(30).seconds.do(FileMonitor, sys.argv[1])

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