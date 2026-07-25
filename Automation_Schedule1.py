# write a program that accept: Msg from user, time interval in sec
# Schedule the program to display msg repeatedly after the specified interval
# Validate that the interval is greater than zero

import schedule
import time

def Display(Message):
    print(Message)

def main():
    Message = input("Enter the Message: ")

    Interval = int(input("Enter interval in seconds: "))

    if Interval <= 0:
        print("Invalid Interval")
        return
    
    schedule.every(Interval).seconds.do(Display,Message)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()
