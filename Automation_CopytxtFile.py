#Write a program that copies all .txt files from one directory to another every 10 min.

import sys
import os
import shutil
import time
import datetime
import schedule

def CopyFiles(SourceDir, DestinationDir):

    if(os.path.exists(SourceDir) == False):
        print("Source directory does not exist")
        return

    if(os.path.exists(DestinationDir) == False):
        os.mkdir(DestinationDir)

    LogFile = open("CopyLog.txt","a")

    LogFile.write("----------------------------------------\n")
    LogFile.write("Copy Time : " + datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p") + "\n")

    for FolderName, SubFolder, FileName in os.walk(SourceDir):

        for File in FileName:

            if(File.endswith(".txt")):

                SourceFile = os.path.join(FolderName, File)
                DestinationFile = os.path.join(DestinationDir, File)

                shutil.copy(SourceFile, DestinationFile)

                LogFile.write(SourceFile + " -> " + DestinationFile + "\n")

    LogFile.close()

    print("All .txt files copied successfully")
    print("----------------------------------------")

def main():

    Border = "-" * 40

    print(Border)
    print(" Marvellous Automation Script ")
    print(Border)

    if(len(sys.argv) == 3):

        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This automation script copies all .txt files every 10 minutes.")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Please execute the script as")
            print("python FileName.py SourceDirectory DestinationDirectory")

        else:

            CopyFiles(sys.argv[1], sys.argv[2])

            schedule.every(10).minutes.do(CopyFiles, sys.argv[1], sys.argv[2])

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