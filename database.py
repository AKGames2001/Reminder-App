from pymongo import MongoClient


class Database:
    def __init__(self):
        self.url = 'mongodb://localhost:27017'
        self.client = MongoClient(self.url)
        if self.client:
            print("Database Connected Successfully")
        self.dbName = self.client['reminderDB']
        self.collection = self.dbName['reminders']

    def insert_user(self, user_data):
        self.collection.insert_one(user_data)

    def insert_reminder(self, user, reminder):
        self.collection.update_one(
            {'name': user},
            {'$push': {'reminders': reminder}}
        )

    def read_database(self):
        items = self.collection.find()
        out_data = []
        for item in items:
            out_data.append(item)
        return out_data

    def update_database(self, query, query_data):
        self.collection.update_one(query, query_data)

    def delete_database(self, user, title):
        self.collection.update_one(
            {'name': user},
            {'$pull': {'reminders': {'title': title}}}
        )

    def delete_user(self, user):
        self.collection.delete_one({'name': user})
        print("Account Successfully Deleted!\nTerminating Program...")
        return True
