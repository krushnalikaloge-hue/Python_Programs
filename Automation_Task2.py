#Schedule a task that executes every 5 min. The task should write current date & time into file named
#Marvellous.txt new entries should be appended without removing previous entries.
#o\p--> task executed at: 25-07-2026 04:30:00 PM

import schedule
import time
import datetime

def Display():
    Current = datetime.datetime.now()

    file = open("Marvellous.txt","a")

    file.write("Task executed at: ")

    file.write(Current.strftime("%d-%m-%Y %I:%M:%S %p"))
    file.write("\n")
    file.close()
    print("Task executed successfully...")

def main():
    schedule.every(5).minutes.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()
