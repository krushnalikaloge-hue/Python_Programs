#Write a program that scans a specific dirctory every min.

import sys
import os
import schedule
import datetime
import time

def DirectoryScanner(DirectoryPath):
    FileCount = 0
    DirectoryCount = 0

    for FolderName, SubFolder, FileName in os.walk(DirectoryPath):
        FileCount = FileCount + len(FileName)
        DirectoryCount = DirectoryCount + len(SubFolder) 

    print("Directory scanned: ",DirectoryPath)
    print("Total Files: ",FileCount)
    print("Total Subdirectories: ",DirectoryCount)
    print("Scan Time: ",datetime.datetime.now())
    print("-------------------------------------------------------")

def main():
    Border = "-"*40

    print(Border)
    print("Marvellous Automation Script")
    print(Border)

    if(len(sys.argv)==2):

        if(sys.argv[1]=="--h" or sys.argv[1]=="--H"):

            print("This script scans the specified directory every one minute. ")
            print("Use --u flag for usage.")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):

            print("Usage: Python FileName.py DirectoryPath")
            print("DirectoryPath should be absolute path.")

        else:

            if(os.path.exists(sys.argv[1]) == False):
                print("Directory does not exist" )
                return

            DirectoryScanner(sys.argv[1])

            schedule.every(1).minutes.do(DirectoryScanner, sys.argv[1])

            while True:
                schedule.run_pending()
                time.sleep(1)

            else:
                print("Invalid number of arguments.")
                print("Use --h or --u flag.")
                print(Border)
                print("Thank you for using Marvellous Automation Script")
                print(Border)

if __name__=="__main__":
    main()