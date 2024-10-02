import sqlite3

# Connect to the SQLite database
connection = sqlite3.connect("student.db")
cursor = connection.cursor()

# Create the STUDENT table if it doesn't exist
table_info = """
CREATE TABLE IF NOT EXISTS STUDENT(
    NAME VARCHAR(25),
    CLASS VARCHAR(25),
    SELECTION VARCHAR(25),
    MARKS INT
);
"""
cursor.execute(table_info)

# Insert initial student records
initial_students = [
    ('darshan', 'python', 'a', 85),
    ('piyush', 'python', 'b', 90),
    ('pranav', 'python', 'e', 85),
    ('pawan', 'python', 'd', 25),
    ('alice', 'java', 'a', 78),
    ('bob', 'java', 'b', 82),
    ('charlie', 'c++', 'c', 91),
    ('dave', 'data science', 'a', 88),
    ('eve', 'web dev', 'b', 76),
    ('frank', 'python', 'd', 55),
    ('grace', 'java', 'e', 92),
    ('hannah', 'c++', 'f', 80),
    ('ivan', 'data science', 'a', 67),
    ('julia', 'web dev', 'b', 89),
    ('karl', 'python', 'a', 72),
    ('lisa', 'java', 'c', 95),
    ('mike', 'c++', 'd', 64),
    ('nina', 'data science', 'e', 90),
    ('oscar', 'web dev', 'f', 83),
    ('paul', 'python', 'a', 73),
    ('quinn', 'java', 'b', 88),
    ('rachel', 'c++', 'c', 70),
    ('sara', 'data science', 'a', 91),
    ('tom', 'web dev', 'b', 82),
    ('uma', 'python', 'e', 79),
    ('vicky', 'java', 'f', 77),
    ('will', 'c++', 'a', 85),
    ('xena', 'data science', 'b', 94),
    ('yara', 'web dev', 'c', 66),
    ('zane', 'python', 'd', 90),
    ('aaron', 'java', 'e', 81),
    ('bela', 'c++', 'f', 93),
    ('carl', 'data science', 'a', 68),
    ('diana', 'web dev', 'b', 86),
    ('edward', 'python', 'c', 74),
    ('flora', 'java', 'd', 97),
    ('george', 'c++', 'e', 63),
    ('hilda', 'data science', 'f', 88),
    ('ira', 'web dev', 'a', 75),
    ('jack', 'python', 'b', 99),
    ('kelly', 'java', 'c', 84),
    ('leo', 'c++', 'd', 71),
    ('mona', 'data science', 'e', 92),
    ('nick', 'web dev', 'f', 60),
    ('olivia', 'python', 'a', 65),
    ('peter', 'java', 'b', 87),
    ('quincy', 'c++', 'c', 90),
    ('riley', 'data science', 'a', 73),
    ('sophie', 'web dev', 'b', 88),
    ('tina', 'python', 'e', 81),
    ('umar', 'java', 'f', 94),
    ('vance', 'c++', 'a', 69),
    ('wade', 'data science', 'b', 80),
    ('xander', 'web dev', 'c', 76),
    ('yasmine', 'python', 'd', 92),
]

# Insert all records into the database
cursor.executemany('INSERT INTO STUDENT VALUES (?, ?, ?, ?)', initial_students)

# Fetch and print all student records
data = cursor.execute('SELECT * FROM STUDENT')
for row in data:
    print(row)

# Commit changes and close the connection
connection.commit()
connection.close()
