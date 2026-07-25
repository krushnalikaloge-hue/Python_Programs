#write a program that schedule the following msg:
#Monday at 9:00 AM: Start your weekly goals
#Wednesday at 5:00 PM: Review your weekly progress
#Friday at 6:00 PM: Weekly work completed

import sys
import os
import schedule

def Mondaymsg():
    print("Start your weekly goals")

def Wednesdaymsg():
    print("Review your weekly progress")

def Fridaymsg():
    print("Weekly work completed")

def main():
    Border = "-"*40

    print(Border)
    print("Marvellous Automation script")
    print(Border)

    if(len(sys.argv)==2):

        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("this automation script display scheduled weekly msg")
            print("For better usage plz check --u flag")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Please execute the script as")
            print("python FileName.py Start")

        else:

            schedule.every().monday.at("09:00").do(Mondaymsg)
            schedule.every().monday.at("17:00").do(Wednesdaymsg)
            schedule.every().monday.at("18:00").do(Fridaymsg)

            while True:
                schedule.run_pending()
                time.sleep(1)

    else:

        print("Invalid No of arguments")
        print("Please use --h or --u for more information")
        print(Border)
        print("Thank you for using Marvellous Automation Script")
        print(Border)

if __name__=="__main__":
    main()