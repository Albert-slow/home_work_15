import sqlite3

connection = sqlite3.connect('bot_users.db', check_same_thread=False)
sql= connection.cursor()

sql.execute('CREATE TABLE IF NOT EXISTS users(name TEXT, id INTEGER, number TEXT, location TEXT);')

def check_user(id):
    check = sql.execute('SELECT * FROM users WHERE id=?;', (id,))
    if check.fetchone():
        return True
    else:
        return False


def register(name, id, number, location):
    sql.execute('INSERT INTO users VALUES(?, ?, ?, ?);', (name, id, number, location))
    connection.commit()



