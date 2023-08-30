import sqlite3


def create_table():
    db = sqlite3.connect('db.db')
    db.execute('''CREATE TABLE IF NOT EXISTS user (name TEXT, help_given INT, help_got INT);''')
    db.commit()
    return db


def add_user(name, db):
    db.execute('''INSERT INTO user (name, help_given, help_got) VALUES (?, ?, ?);''', (name, 0, 0))
    db.commit()


def user_exists(name, db):
    cursor = db.execute('''SELECT * FROM user WHERE name=?;''', (name,))
    return len(cursor.fetchall()) > 0


def main():
    db = create_table()
    add_user('test', db)
    db.close()


if __name__ == '__main__':
    main()