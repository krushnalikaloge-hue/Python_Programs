#write program that accept a directory name from user and count number of files inside it every 10 min.

import sys
import os
import time
import datetime
import schedule

def DirectoryCount(DirectoryPath):

    FileCount = 0

    for FolderName, SubFolder, FileName in os.walk(DirectoryPath):
        FileCount = FileCount + len(FileName)

    fobj = open("DirectoryCountLog.txt", "a")

    fobj.write("Directory Path : " + DirectoryPath + "\n")
    fobj.write("Number of Files : " + str(FileCount) + "\n")
    fobj.write("Date and Time : " + datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p") + "\n")
    fobj.write("----------------------------------------\n")

    fobj.close()

    print("Directory Path :", DirectoryPath)
    print("Number of Files :", FileCount)
    print("Information stored in DirectoryCountLog.txt")
    print("----------------------------------------")

def main():

    Border = "-" * 40

    print(Border)
    print(" Marvellous Automation Script ")
    print(Border)

    if(len(sys.argv) == 2):

        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This automation script counts the files in a directory every 5 minutes.")
            print("For better usage please check --u flag")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Please execute the script as")
            print("python FileName.py DirectoryPath")
            print("DirectoryPath should be absolute path")

        else:

            if(os.path.exists(sys.argv[1]) == False):
                print("Directory does not exist")
                return

            DirectoryCount(sys.argv[1])

            schedule.every(10).minutes.do(DirectoryCount, sys.argv[1])

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