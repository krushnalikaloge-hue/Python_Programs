#write program that creae a new log file after every ten minutes.

import sys
import os
import time
import datetime
import schedule

def CreateLogFile():

    CurrentTime = datetime.datetime.now()

    FileName = "MarvellousLog_" + CurrentTime.strftime("%d_%m_%Y_%H_%M_%S") + ".txt"

    fobj = open(FileName, "w")

    fobj.write("Log file created successfully.\n")
    fobj.write("Creation Time : ")
    fobj.write(CurrentTime.strftime("%d-%m-%Y %I:%M:%S %p"))

    fobj.close()

    print("Log file created successfully.")
    print("Creation Time :", CurrentTime.strftime("%d-%m-%Y %I:%M:%S %p"))
    print("----------------------------------------")

def main():

    Border = "-" * 40

    print(Border)
    print(" Marvellous Automation Script ")
    print(Border)

    if(len(sys.argv) == 2):

        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This automation script creates a new log file every 10 minutes.")
            print("For better usage please check --u flag")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Please execute the script as")
            print("python FileName.py Start")

        else:

            CreateLogFile()

            schedule.every(1).minutes.do(CreateLogFile)

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