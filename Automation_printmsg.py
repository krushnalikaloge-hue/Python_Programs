# Write a Python program that prints: Jay Ganesh...  every 2 sec

import schedule
import time

def Display():
    print("Jay Ganesh...")

def main():
    print("Automation Script started")

    schedule.every(2).seconds.do(Display)

    while True:
       schedule.run_pending()
       time.sleep(1)

    print("End of Automation script")

if __name__=="__main__":
    main()