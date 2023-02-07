# Reminder-App
Desktop Reminder App for Windows based on Python and Tkinter

# PRE-REQUISITS:
    Download MonogDB Server from the following link:
        https://www.mongodb.com/try/download/community
    Install the MongoDB by follwing all the instructions.
    After Installation, open Terminal/Cmd. Create the directory data\db in the default location.
    Start the server using following command:
        [For Windows (if using default directory)]
        "C:\Program Files\MongoDB\Server\<insert version number>\bin\mongod.exe"

# APPLICATION :-
    To initialize the app, run the "main.py" using the IDLE or terminal
    Once work is finished quit the application

# REMINDER SYSTEM :-
    To initialize the reminder system, run the "notification.py" using following command in Command Prompt or Terminal :
        $ pythonw.exe .\notification.py

    This will generate a system-wide service which will monitor your reminders and alert them time to time
	
    To deactivate reminder system, simply open Task Manager and End Task the running "Python <ver> (windowed)" process
