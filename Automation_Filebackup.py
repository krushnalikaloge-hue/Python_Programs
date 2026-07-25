# write the backup operation details into:
# backup_log.txt: Example backup filename
# Data_25_07_2026_16_30_00.txt: Example log entry
# Backup completed successfully at 25_07_2026 04:30:00 PM
# Use the shutil module for file copying.

import schedule
import time
import os
import datetime
import shutil

def Backup():
    Source = input("Enter source file path name: ")

    Destination = input("Enter the destination directory path:")
    
    CurrentTime = datetime.datetime.now()

    Filename = os.path.basename(Source)

    Name, Extension = os.path.splitext(Filename)

    BackupFile = Name + "_"+ CurrentTime.strftime("%d_%m_%Y-%H_%M_%S")+ Extension

    DestinationPath = os.path.join(Destination,BackupFile)

    shutil.copy(Source,DestinationPath)

    fobj = open("backup_log.txt","a")

    fobj.write("Backup completed successfully at "+CurrentTime.strftime("%d_%m_%Y %I:%M:%S %p")+"\n")

    fobj.close()

def main():
    schedule.every(2).minutes.do(Backup)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()