import sqlite3
connection=sqlite3.connect("student.db")
cursor=connection.cursor()
table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),SELECTION VARCHAR(25),MARKS INT);



"""
# cursor.execute(table_info)
cursor.execute(f"PRAGMA table_info({'STUDENT'})")
schema_info = cursor.fetchall()
print(schema_info)
cursor.execute('''Insert Into STUDENT values('darshan','python','a',85) ''')
cursor.execute('''Insert Into STUDENT values('piyusf','python','b',90) ''')
cursor.execute('''Insert Into STUDENT values('pranav','python','e',85) ''')
cursor.execute('''Insert Into STUDENT values('pawan','python','d',25) ''')
data=cursor.execute('''Select * From STUDENT''')
for row in data:
    print(row)


connection.commit()
connection.close()