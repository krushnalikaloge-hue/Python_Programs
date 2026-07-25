# write a script that schedule the following task: 
# print Lunch Time ! every day at 1.00 PM
# print wrap up work every day at 6.00 PM

import schedule
import time

def Lunch():
    print("Lunch Time!")

def Wrapup():
    print("Wrap up work")

def main():
    schedule.every().day.at("13:00").do(Lunch)
    schedule.every().day.at("18:00").do(Wrapup)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()