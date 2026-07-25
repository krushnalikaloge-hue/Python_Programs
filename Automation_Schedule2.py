# Create a function named: DisplayMessage(message)Schedule the function using: 

import schedule
import time

def DisplayMessage(message):
    print(message)

def main():
    message = input("Enter the Message: ")

    schedule.every(5).seconds.do(DisplayMessage, message)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()
