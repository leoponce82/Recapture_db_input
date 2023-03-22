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

c.execute(" INSERT INTO users VALUES ('admin','admin',)")

conn.commit()

conn.close()