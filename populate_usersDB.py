import sqlite3

conn = sqlite3.connect("users.db")

c = conn.cursor()

c.execute(
    """CREATE TABLE users (
        first_name text,
        last_name text,
        email text
        
        )"""
)


conn.commit()

conn.close()
