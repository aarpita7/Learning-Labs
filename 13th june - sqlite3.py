import sqlite3

# Connect to a SQLite database or create it if it doesn't exist
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Creating a table
cursor.execute('''
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    email TEXT NOT NULL
)
''')
conn.commit()

# Inserting multiple values into the table
users = [
    ('Arpita', 30, 'arpita@example.com'),
    ('Sunita', 25, 'sunita@example.com'),
    ('Shivam', 35, 'shivam@example.com')
]
cursor.executemany('''
INSERT INTO users (name, age, email) VALUES (?, ?, ?)
''', users)
conn.commit()

# Querying data with a specific condition
cursor.execute('SELECT * FROM users WHERE age > 30')
rows = cursor.fetchall()
print("Users older than 30:")
for i in rows:
    print(i)

# Updating data for a specific user
cursor.execute('''
UPDATE users SET email = ? WHERE name = ?
''', ('arpita@example.com', 'Arpita'))
conn.commit()

# Querying all data to see the update
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()
print("All users after update:")
for i in rows:
    print(i)

# Deleting data for a specific user
cursor.execute('''
DELETE FROM users WHERE name = ?
''', ('Shivam',))
conn.commit()

# Closing the connection
cursor.close()
conn.close()
