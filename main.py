import os
import shutil
import datetime
import time
import schedule

source_dir=r"C:\Users\STAR COMPUTER SYSTEM\Music"
destination_dir=r"D:\Backup"

def copy(source,destination):
    today=datetime.date.today()
    dest_dir=os.path.join(destination,str(today))

    try:
        shutil.copytree(source,dest_dir)
        print(f"Backup completed\n Folder copied to {dest_dir}")
    except FileExistsError as e:
        print("File already exists")
    except FileNotFoundError as e:
        print ("FIle not found")
schedule.every().day.at("18:27").do(lambda:copy(source_dir,destination_dir))

while True:
    schedule.run_pending()
    time.sleep(60)

copy(source_dir,destination_dir)