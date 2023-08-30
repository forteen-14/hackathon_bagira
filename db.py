import sqlite3

class DataBase:
    def __init__(self):
        self.db = self.create_table()
    def create_table(self):
        db = sqlite3.connect('db.db',check_same_thread=False)
        db.execute('''CREATE TABLE IF NOT EXISTS user (name TEXT, help_given INT, help_got INT);''')
        db.commit()
        return db


    def add_user(self,name):
        self.db.execute('''INSERT INTO user (name, help_given, help_got) VALUES (?, ?, ?);''', (name, 0, 0))
        self.db.commit()


    def user_exists(self,name):
        cursor = self.db.execute('''SELECT * FROM user WHERE name=?;''', (name,))
        return len(cursor.fetchall()) > 0


    def get_all_data_by_name(self,name):
        cursor = self.db.execute('''SELECT * FROM user WHERE name=?;''', (name,))
        return cursor.fetchall()[0]

    def close(self):
        self.db.close()





