from database import Database


class Users:
    def __init__(self):
        self.db = Database()
        self.users = self.db.read_database()

    def register_gui(self, username, password):
        available = False
        for user in self.users:
            if username == user['name']:
                available = False
                return 'taken'
            else:
                available = True
        if available:
            user = {
                'name': username,
                'password': password,
                'reminders': []
            }
            self.db.insert_user(user)
            return user['name']

    def login_gui(self, username, password):
        variable = 0
        for user in self.users:
            try:
                if username == user['name']:
                    idx = variable
                    if password == self.users[idx]['password']:
                        return 'login'
                    else:
                        return 'wrong_password'
            except KeyError:
                print(user)
            finally:
                variable += 1
        return 'no_user'

    def deactivate_gui(self, user):
        self.db.delete_user(user)
        return True

