import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="SampleDB"
)

cur = conn.cursor()

cur.execute("Select * from students")

result = cur.fetchall()

print("Student details are:")

for x in result:
    print(x)
conn.commit()
conn.close()
