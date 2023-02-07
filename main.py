from tkinter import *
from tkcalendar import Calendar
from datetime import date
from reminder import Reminders
from users import Users
from PIL import ImageTk, Image


class ReminderApp:
    def __init__(self):
        self.root = Tk()
        TITLE = "ReminderApp"
        GEOMETRY = "600x400"
        self.root.withdraw()

        self.main_window = Toplevel()
        self.main_window.title(TITLE)
        self.main_window.geometry(GEOMETRY)
        self.main_window.wm_attributes('-transparentcolor', '#ab23ff')

        self.login_window = Toplevel()
        self.login_window.title(TITLE)
        self.login_window.geometry(GEOMETRY)
        self.login_window.withdraw()

        self.register_window = Toplevel()
        self.register_window.title(TITLE)
        self.register_window.geometry(GEOMETRY)
        self.register_window.withdraw()

        self.app_window = Toplevel()
        self.app_window.title(TITLE)
        self.app_window.geometry(GEOMETRY)
        self.app_window.withdraw()

        self.delete_user_window = Toplevel()
        self.delete_user_window.title(TITLE)
        self.delete_user_window.geometry("300x200")
        self.delete_user_window.withdraw()

        self.app_add_window = Toplevel()
        self.app_add_window.title(TITLE)
        self.app_add_window.geometry(GEOMETRY)
        self.app_add_window.withdraw()

        self.app_view_window = Toplevel()
        self.app_view_window.title(TITLE)
        self.app_view_window.geometry(GEOMETRY)
        self.app_view_window.withdraw()

        self.app_delete_window = Toplevel()
        self.app_delete_window.title(TITLE)
        self.app_delete_window.geometry(GEOMETRY)
        self.app_delete_window.withdraw()

        self.user = Users()
        self.app = Reminders()
        self.current_user = None
        self.is_app = True
        self.is_auth = False

        self.main_window.deiconify()
        self.first_window()
        self.root.mainloop()

    # TODO : [First Window] Fix the Image
    def first_window(self):
        def check_decision(decision):
            if decision == 'login':
                self.main_window.withdraw()
                self.login_window.deiconify()
                self.second_window()
            else:
                self.main_window.withdraw()
                self.register_window.deiconify()
                self.third_window()

        C = Canvas(self.main_window, bg="blue", height=300, width=600)

        # filename = ImageTk.PhotoImage(Image.open("images/main-background-2.jpg"))
        img = Image.open("images/main-background-2.jpg")
        resized_image = img.resize((1050, 600), Image.LANCZOS)
        new_image = ImageTk.PhotoImage(resized_image)
        C.create_image(300, 600, image=new_image)
        C.create_text(285, 150, fill="white", font="Arial 28 bold",
                      text="  Welcome to\nReminder App")
        C.grid(row=0, column=0, columnspan=3)

        blankLabel = Label(
            self.main_window,
            text="",
            padx=5,
            pady=5
        )
        blankLabel.grid(row=1, column=0, columnspan=3)

        loginButton = Button(
            self.main_window,
            text="Login",
            height=2,
            width=12,
            command=lambda: check_decision('login')
        )
        loginButton.grid(row=2, column=0)

        orLabel = Label(
            self.main_window,
            text="OR"
        )
        orLabel.grid(row=2, column=1)

        registerButton = Button(
            self.main_window,
            text="Register",
            height=2,
            width=12,
            command=lambda: check_decision('register'),
            font=("Arial", 8)
        )
        registerButton.grid(row=2, column=2)

    def second_window(self):
        def check_login(e, u, p):
            userName = u.get()
            passWord = p.get()
            auth = self.user.login_gui(userName, passWord)
            if auth == 'login':
                self.is_app = False
                self.current_user = userName
                self.login_window.withdraw()
                self.app_window.deiconify()
                self.fourth_window()
            elif auth == 'wrong_password':
                e["text"] = "Wrong Password!\nPlease login again"
            elif auth == 'no_user':
                e["text"] = "No such user found!\nPlease register for app"

        image1 = Image.open("images/reminder-login.png")
        image1 = image1.resize((400, 400), Image.LANCZOS)

        test = ImageTk.PhotoImage(image1)

        image_label = Label(self.login_window, image=test)
        image_label.image = test
        image_label.grid(row=0, column=0, rowspan=5)

        errorLabel = Label(
            self.login_window,
            text="",
            height=2,
        )
        errorLabel.grid(row=0, column=1)

        label2 = Label(
            self.login_window,
            text="Login",
            font=("Arial", "24", "bold"),
            padx=27
        )
        label2.grid(row=1, column=1, padx=(30, 20), pady=(5, 5))

        usernameFrame = Frame(
            self.login_window,
            relief="solid"
        )
        usernameLabel = Label(
            usernameFrame,
            text="Username"
        )
        usernameEntry = Entry(usernameFrame)

        usernameLabel.pack(side="top", fill="both", expand=True)
        usernameEntry.pack(side="top", fill="x")

        usernameFrame.grid(row=2, column=1)

        passwordFrame = Frame(
            self.login_window,
            relief="solid"
        )
        passwordLabel = Label(
            passwordFrame,
            text="Password"
        )
        passwordEntry = Entry(passwordFrame)

        passwordLabel.pack(side="top", fill="both", expand=True)
        passwordEntry.pack(side="top", fill="x")

        passwordFrame.grid(row=3, column=1)

        loginButton = Button(
            self.login_window,
            text="login",
            height=1,
            width=8,
            font=("Arial", 10),
            command=lambda: check_login(errorLabel, usernameEntry, passwordEntry)
        )
        loginButton.grid(row=4, column=1)

    def third_window(self):
        def passWord_valid(password, e, u):
            if len(password) < 8:
                e['text'] = "Password must be\n8 char or larger"
                return False
            if password == u:
                e['text'] = "Password can't be Username\nTry something else."
                return False
            if not password.isalnum():
                e['text'] = "Use only Alphabets &\nNumbers for Password"
                return False
            return True

        def do_register(e, u, p, c):
            userName = u.get()
            if userName == "" or not userName.isalpha():
                e['text'] = "Enter valid Username"
                return None
            passWord = p.get()
            if passWord == "":
                e['text'] = "Enter valid Password"
                return None
            elif not passWord_valid(passWord, e, userName):
                return None
            cnfPassword = c.get()
            if cnfPassword == "" or cnfPassword != passWord:
                e['text'] = "Enter correct\nConfirm Password"
                return None
            user = self.user.register_gui(userName, passWord)
            if user == userName:
                self.is_app = False
                self.current_user = user
                self.register_window.withdraw()

                self.app_window.deiconify()
                self.fourth_window()
            elif user == 'taken':
                e['text'] = "Username already Taken\nTry another one"
            else:
                e['text'] = "Unknown Error Occurred"

        image1 = Image.open("images/reminder-login.png")
        image1 = image1.resize((400, 400), Image.LANCZOS)

        test = ImageTk.PhotoImage(image1)

        image_label = Label(self.register_window, image=test)
        image_label.image = test
        image_label.grid(row=0, column=0, rowspan=6)

        errorLabel = Label(
            self.register_window,
            text="",
            height=2
        )
        errorLabel.grid(row=0, column=1)

        label2 = Label(
            self.register_window,
            text="Register",
            font=("Arial", "24", "bold")
        )
        label2.grid(row=1, column=1, padx=(30, 20), pady=(5, 5))

        usernameFrame = Frame(
            self.register_window,
            relief="solid"
        )
        usernameLabel = Label(
            usernameFrame,
            text="Username"
        )
        usernameEntry = Entry(usernameFrame)

        usernameLabel.pack(side="top", fill="both", expand=True)
        usernameEntry.pack(side="top", fill="x")

        usernameFrame.grid(row=2, column=1)

        passwordFrame = Frame(
            self.register_window,
            relief="solid"
        )
        passwordLabel = Label(
            passwordFrame,
            text="Password"
        )
        passwordEntry = Entry(passwordFrame)

        passwordLabel.pack(side="top", fill="both", expand=True)
        passwordEntry.pack(side="top", fill="x")

        passwordFrame.grid(row=3, column=1)

        confPasswordFrame = Frame(
            self.register_window,
            relief="solid"
        )
        confPasswordLabel = Label(
            confPasswordFrame,
            text="Confirm Password"
        )
        confPasswordEntry = Entry(confPasswordFrame)

        confPasswordLabel.pack(side="top", fill="both", expand=True)
        confPasswordEntry.pack(side="top", fill="x")

        confPasswordFrame.grid(row=4, column=1)

        registerButton = Button(
            self.register_window,
            text="Register",
            height=1,
            width=8,
            font=("Arial", 10),
            command=lambda: do_register(errorLabel, usernameEntry, passwordEntry, confPasswordEntry)
        )
        registerButton.grid(row=5, column=1)

    def fourth_window(self):
        def delete_user():
            if self.user.deactivate_gui(self.current_user):
                self.root.destroy()

        def check_decision(decision):
            if decision == 'add':
                self.app_window.withdraw()
                self.app_add_window.deiconify()
                self.fourth_window_add()

            elif decision == 'view':
                self.app_window.withdraw()
                self.app_view_window.deiconify()
                self.fourth_window_view()

            elif decision == 'delete':
                self.app_window.withdraw()
                self.app_delete_window.deiconify()
                self.fourth_window_delete()

            elif decision == "logout":
                self.root.destroy()

            elif decision == 'delete_user':
                self.delete_user_window.deiconify()

                confirmationLabel = Label(
                    self.delete_user_window,
                    text="Do you really want\nto Delete your account?",
                    height=2
                )
                confirmationLabel.grid(row=0, column=0, columnspan=2, padx=(40, 0), pady=(35, 20))

                yesButton = Button(
                    self.delete_user_window,
                    text="Yes",
                    height=1,
                    width=8,
                    font=("Arial", 10),
                    command=lambda: delete_user()
                )
                yesButton.grid(row=1, column=0, pady=(20, 30), padx=(60, 15))

                noButton = Button(
                    self.delete_user_window,
                    text="No",
                    height=1,
                    width=8,
                    font=("Arial", 10),
                    command=lambda: self.delete_user_window.withdraw()
                )
                noButton.grid(row=1, column=1, pady=(20, 30), padx=(15, 40))

        addButton = Button(
            self.app_window,
            text="Add Reminder",
            height=1,
            width=5,
            padx=30,
            command=lambda: check_decision('add')
        )
        addButton.grid(row=0, column=0, padx=(70, 30), pady=(70, 45))

        viewButton = Button(
            self.app_window,
            text="View Reminders",
            height=1,
            width=5,
            padx=30,
            command=lambda: check_decision('view')
        )
        viewButton.grid(row=1, column=0, padx=(70, 30), pady=(45, 30))

        deleteButton = Button(
            self.app_window,
            text="Delete Reminder",
            height=1,
            width=5,
            padx=30,
            command=lambda: check_decision('delete')
        )
        deleteButton.grid(row=2, column=0, padx=(70, 30), pady=(20, 0))

        logoutButton = Button(
            self.app_window,
            text="Logout",
            height=1,
            width=5,
            padx=30,
            command=lambda: check_decision('logout')
        )
        logoutButton.grid(row=3, column=0, padx=(70, 30), pady=(35, 0))

        image1 = Image.open("images/user-image.png")
        image1 = image1.resize((150, 150), Image.LANCZOS)

        test = ImageTk.PhotoImage(image1)

        image_label = Label(self.app_window, image=test)
        image_label.image = test
        image_label.grid(row=0, column=1, padx=(100, 50), pady=(20, 0))

        nameLabel = Label(
            self.app_window,
            text=self.current_user,
            font=("Arial", "18", "bold")
        )
        nameLabel.grid(row=1, column=1, padx=(100, 50), pady=(20, 0))

        reminderCountLabel = Label(
            self.app_window,
            text="number of reminders",
        )
        reminderCountLabel.grid(row=2, column=1, padx=(100, 50), pady=(20, 0))

        deleteUserButton = Button(
            self.app_window,
            text="Delete User",
            height=1,
            width=5,
            padx=30,
            command=lambda: check_decision('delete_user')
        )
        deleteUserButton.grid(row=3, column=1, padx=(75, 30), pady=(35, 0))

    def fourth_window_add(self):
        def previous_page():
            self.app_add_window.withdraw()
            self.app_window.deiconify()
            self.fourth_window()

        def add_reminder(t, c, e):
            reqDate = c.get_date()
            title = t.get("1.0", END).split("\n")
            if title[0] == "":
                e['text'] = "Please enter Valid\nTitle of Reminder"
                return None
            else:
                self.app.add_reminder_gui(self.current_user, title[0], reqDate)
                self.app_add_window.withdraw()
                self.app_window.deiconify()
                self.fourth_window()

        titleLabel = Label(
            self.app_add_window,
            text="Add Reminder",
            font=("Arial", 24, "bold")
        )
        titleLabel.grid(row=0, column=0, padx=(30, 30), pady=(30, 20))

        errorLabel = Label(
            self.app_add_window,
            text="",
            height=2
        )
        errorLabel.grid(row=0, column=1, padx=(30, 30), pady=(30, 20))

        reminderTitleLabel = Label(
            self.app_add_window,
            text="Title of Reminder",
        )
        reminderTitleLabel.grid(row=1, column=0)

        reminderTitleInput = Text(
            self.app_add_window,
            height=1,
            width=35
        )
        reminderTitleInput.grid(row=1, column=1)

        reminderDateLabel = Label(
            self.app_add_window,
            text="Date (MM/DD/YY)",
        )
        reminderDateLabel.grid(row=2, column=0)

        dt = date.today()

        currentYear = int(dt.year)
        currentMonth = int(dt.month)
        currentDay = int(dt.day)

        cal = Calendar(self.app_add_window, selectmode='day',
                       year=currentYear,
                       month=currentMonth,
                       day=currentDay)

        cal.grid(row=2, column=1, pady=(20, 20))

        submitButton = Button(
            self.app_add_window,
            text="Add",
            width=4,
            padx=30,
            command=lambda: add_reminder(reminderTitleInput, cal, errorLabel)
        )
        submitButton.grid(row=3, column=1)

        backButton = Button(
            self.app_add_window,
            text="Back",
            width=4,
            padx=30,
            command=lambda: previous_page()
        )
        backButton.grid(row=3, column=0)

    def fourth_window_view(self):
        DATA_COUNT = 0

        def refresh_data(count, t, d):
            for _ in range(count):
                t.destroy()
                d.destroy()
            count = 0

            data = self.app.view_reminders_gui()
            total_rows = len(data)
            for i in range(total_rows):
                if data[i]['name'] == self.current_user:
                    x = i
                    total_reminders = len(data[x]['reminders'])
                    for j in range(total_reminders):
                        titleLabelGui = Label(
                            self.app_view_window,
                            text=data[x]['reminders'][j]['title'],
                            font=('Arial', 12)
                        )
                        titleLabelGui.grid(row=j + 3, column=0)
                        dateLabelGui = Label(
                            self.app_view_window,
                            text=data[x]['reminders'][j]['date'],
                            font=('Arial', 12)
                        )
                        dateLabelGui.grid(row=j + 3, column=1, columnspan=2, padx=(20, 20), pady=(5, 5))

                        count += 1

        def previous_page():
            self.app_view_window.withdraw()
            self.app_window.deiconify()
            self.fourth_window()

        titleLabel = Label(
            self.app_view_window,
            text="View Reminders",
            font=("Arial", 24, "bold")
        )
        titleLabel.grid(row=0, column=0, padx=(20, 10), pady=(10, 10))

        backButton = Button(
            self.app_view_window,
            text="Back",
            command=lambda: previous_page(),
            height=2,
            width=12,
        )
        backButton.grid(row=0, column=2, padx=(10, 0))

        refreshButton = Button(
            self.app_view_window,
            text="Refresh",
            command=lambda: refresh_data(DATA_COUNT, titleLabelGui, dateLabelGui),
            height=2,
            width=12
        )
        refreshButton.grid(row=0, column=1, padx=(50, 10))

        errorLabel = Label(
            self.app_view_window,
            text=""
        )
        errorLabel.grid(row=1, column=0, columnspan=3)

        titleLabelChart = Label(
            self.app_view_window,
            text="Title",
            font=("Arial", 16)
        )
        titleLabelChart.grid(row=2, column=0)

        dateLabelChart = Label(
            self.app_view_window,
            text="Date",
            font=("Arial", 16)
        )
        dateLabelChart.grid(row=2, column=1, columnspan=2)

        data = self.app.view_reminders_gui()
        total_rows = len(data)
        for i in range(total_rows):
            if data[i]['name'] == self.current_user:
                x = i
                total_reminders = len(data[x]['reminders'])
                for j in range(total_reminders):
                    titleLabelGui = Label(
                        self.app_view_window,
                        text=data[x]['reminders'][j]['title'],
                        font=('Arial', 12)
                    )
                    titleLabelGui.grid(row=j + 3, column=0)
                    dateLabelGui = Label(
                        self.app_view_window,
                        text=data[x]['reminders'][j]['date'],
                        font=('Arial', 12)
                    )
                    dateLabelGui.grid(row=j + 3, column=1, columnspan=2, padx=(20, 20), pady=(5, 5))

                    DATA_COUNT += 1

    def fourth_window_delete(self):
        def previous_page():
            self.app_delete_window.withdraw()
            self.app_window.deiconify()
            self.fourth_window()

        def delete_reminder(n):
            numberOfReminder = n.get("1.0", END).split()
            self.app.delete_reminders_gui(self.current_user, int(numberOfReminder[0]))
            self.app_delete_window.withdraw()
            self.app_window.deiconify()
            self.fourth_window()

        titleLabel = Label(
            self.app_delete_window,
            text="Delete Reminder",
            font=("Arial", "24", "bold")
        )
        titleLabel.grid(row=0, column=0, padx=(30, 30), pady=(30, 20))

        errorLabel = Label(
            self.app_delete_window,
            text="",
            height=2
        )
        errorLabel.grid(row=0, column=1, padx=(30, 30), pady=(30, 20))

        reminderTitleLabel = Label(
            self.app_delete_window,
            text="Number of Reminder",
        )
        reminderTitleLabel.grid(row=1, column=0)

        reminderTitleInput = Text(
            self.app_delete_window,
            height=1,
            width=28
        )
        reminderTitleInput.grid(row=1, column=1)

        submitButton = Button(
            self.app_delete_window,
            text="Delete",
            width=4,
            padx=30,
            command=lambda: delete_reminder(reminderTitleInput)
        )
        submitButton.grid(row=2, column=0, columnspan=2, padx=(50, 50), pady=(25, 50))

        backButton = Button(
            self.app_delete_window,
            text="Back",
            width=4,
            padx=30,
            command=lambda: previous_page()
        )
        backButton.grid(row=3, column=0, columnspan=2, padx=(50, 50), pady=(120, 10))


if __name__ == "__main__":
    ReminderApp()
