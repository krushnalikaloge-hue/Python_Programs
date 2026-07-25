#write a program that createsa new text file every minute.

import sys
import time
import datetime
import schedule

def CreateFile():
    CurrentTime = datetime.datetime.now()

    FileName = "File_"+ CurrentTime.strftime("%d_%m_%Y_%H_%M_%S") + ".txt"

    fobj = open(FileName,"w")

    fobj.write("File Name: " + FileName + "\n")

    fobj.write("Creation Date: " + CurrentTime.strftime("%d-%m-%Y") + "\n")

    fobj.write("Creation Time: " + CurrentTime.strftime("%I:%M:%S %p") + "\n")

    fobj.close()

    print("File created successfully: ",FileName)

    print("-------------------------------------------------------------------")

def main():

    Border = "-" * 40

    print(Border)

    print("Marvellous Automation Script")

    print(Border)

    if(len(sys.argv) == 2):

        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):

            print("This automation script creates a new text file every minute.")
            print("For better usage please check --u flag")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
             
            print("Please execute the script as")
            print("Python FileName.py Start")

        else:
            CreateFile()
        
    schedule.every(1).minutes.do(CreateFile)

    while True:
        schedule.run_pending()
        time.sleep(1)
    
    else:
        print("Invalid number of arguments")
        print("Thank you for using Marvellous Automation Script")
        print(Border)

if __name__=="__main__":
    main()