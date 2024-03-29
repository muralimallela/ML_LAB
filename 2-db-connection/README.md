# Setting Up SampleDB Database and students Table

This guide will walk you through setting up the `SampleDB` database and creating the `students` table using MySQL.

## Prerequisites

Before you start, ensure you have MySQL installed on your system.

## Installing mysql.connector

Before executing the script, make sure to install `mysql.connector` using pip. You can do this by running the following command:

```bash
pip install mysql.connector
```

## Steps

1. Open your MySQL command-line client or any MySQL database management tool.

2. Run the following commands to create the database and switch to it:

    ```sql
    CREATE DATABASE IF NOT EXISTS `SampleDB`;
    USE `SampleDB`;
    ```

3. Once you've selected the `SampleDB` database, run the following SQL query to create the `students` table:

    ```sql
    CREATE TABLE `students` (
      `sid` varchar(10) DEFAULT NULL,
      `sname` varchar(10) DEFAULT NULL,
      `age` int(11) DEFAULT NULL
    );
    ```

4. Now, you can populate the `students` table with sample data by executing the following SQL query:

    ```sql
    INSERT INTO `students` (`sid`, `sname`, `age`) VALUES
    ('s521', 'Jhon Bob', 23),
    ('s522', 'Dilly', 22),
    ('s523', 'Kenney', 25),
    ('s524', 'Herny', 26);
    ```

5. Once the table is created and populated, you can use it in your applications.

## Usage

You can use the provided Python script `dbConnect.py` to connect to the `SampleDB` database and retrieve student details. Make sure to update the connection parameters in the script according to your MySQL setup.

```python
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="SampleDB"
)

cur = conn.cursor()

cur.execute("SELECT * FROM students")

result = cur.fetchall()

print("Student details are:")

for x in result:
    print(x)

conn.commit()
conn.close()
```
