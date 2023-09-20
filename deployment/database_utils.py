import sqlite3

# variable's
connection = sqlite3.connect('user_logs.db', timeout=1, check_same_thread=False)
cursor = connection.cursor()


def create_database():
    # create table
    try:
        cursor.execute(f'CREATE TABLE IF NOT EXISTS idpass (id INTEGER PRIMARY KEY, email TEXT NOT NULL UNIQUE, pass TEXT NOT NULL, level TEXT NOT NULL) ')
        connection.commit()
    except Exception as e: 
        print('Table idpass is NOT created : \n',e)

