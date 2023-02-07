from database import Database


class Reminders:
    def __init__(self):
        self.reminders = []
        self.db = Database()

    def add_reminder_gui(self, user, title, date):
        out_dict = {
            'title': title,
            'date': date
        }
        self.db.insert_reminder(user, out_dict)

    def view_reminders_gui(self):
        data = self.db.read_database()
        return data

    def delete_reminders_gui(self, user, num):
        data = self.db.read_database()
        for i in data:
            if i['name'] == user:
                reminders = i['reminders']
                rem_to_delete = reminders[num-1]
                title = rem_to_delete['title']
                self.db.delete_database(user, title)
