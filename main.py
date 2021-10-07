import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Please Drink Water Now !!",
            message = "Health experts commonly recommend eight 8-ounce glasses, which equals about 2 liters, or half a gallon a day.",
            app_icon = "water.ico ",
            timeout = 10
        )
        time.sleep(60*60) # after 1 hour.
     
     #pythonw.exe .\main.py
     # then delete from Task management (file name: python)