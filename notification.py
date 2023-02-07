from datetime import date
import time
from plyer import notification
from database import Database
from messenger import Twilio

db = Database()
sms = Twilio()


def send_notification(r, d):
    notification.notify(

        # defining the title of the notification
        title=r['title'],

        # defining the message of the notification
        message=f"{d}  ~Python Reminder",

        # creating icon for the notification
        # we have to download an icon of .ico file format
        # app_icon="covidProtection.ico",

        # the notification stays for 30 seconds
        timeout=10
    )


def send_sms(r):
    # for testing purposes, I haven't included phone number while registering user
    # Edit the string below with phone number for testing purpose
    testNumber = ""
    
    sms.send_message(r['title'], testNumber)


while True:
    # today's date
    d_today = date.today()

    # mm/dd/yy
    today = d_today.strftime("%m/%d/%y")

    # check the database
    data = db.read_database()
    for i in data:
        reminders = i['reminders']
        for reminder in reminders:
            date = reminder['date']
            if date == today:
                send_notification(reminder, today)
                send_sms(reminder) # Disable this if you do not want to send SMS

    # sleep for 12 hrs => 60 * 60 * 12 seconds
    # notification repeats after every 12 hours
    time.sleep(60 * 60 * 12)
