# write python program that display current date and time after every 1 min

import schedule
import time
import datetime

def Display():
    Current = datetime.datetime.now()
    # %d=date  %m=month  %Y=Year  %I=Hour  %M=Minutes  %S=Seconds  %p=+AM/PM
    print("Current Date and Time: ",Current.strftime("%d-%m-%Y %I:%M:%S %p"))
    
def main():
    schedule.every(1).minutes.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)
    
if __name__=="__main__":
    main()