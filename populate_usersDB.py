import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

conn = sqlite3.connect("users.db")

c = conn.cursor()

c.execute(
    """CREATE TABLE users (
        user_name text PRIMARY KEY,
        email text,
        user_password text
        )"""
)

# c.execute(" INSERT INTO users VALUES ('admin','admin',)")

conn.commit()

conn.close()