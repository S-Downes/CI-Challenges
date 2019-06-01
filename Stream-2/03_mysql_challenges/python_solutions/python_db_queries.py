# !/usr/bin/env python
import os
import pymysql
import datetime

# Get the username from the Cloud9 workspace (modify this variable if running on another environment)
username = os.getenv('C9_USER')

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='Chinook')

""" Step 1 - Print data
try:
    # Run a query
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()
""" 

""" Step 2 - Return data in dict format
try:
    # Run a query
    # Returns data in dict format
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = "SELECT * FROM Artist;"
        cursor.execute(sql)
        for row in cursor:
            print(row)
finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()
"""

""" Step 3 - Create a table
try:
    # Run a query
    with connection.cursor() as cursor:
        cursor.execute('''CREATE TABLE IF NOT EXISTS
                          Friends(name char(20), age int, DOB datetime);''')
        # Note that the above will still display a warning (not error) if the
        # table already exists
finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()
"""

""" Step 4 - Insert values into the Friends table
try:
    # Run a query
    with connection.cursor() as cursor:
        row = ("jim", 27, "1991-02-06 23:04:56")
        cursor.execute('''Insert Into Friends Values (%s, %s, %s);''', row)
        connection.commit()
finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()
"""

""" Step 5 - Add multiple rows to the table using executemany
try:
    # Run a query
    with connection.cursor() as cursor:
        rows = [("john", 21, "1990-02-06 23:04:56"),
                ("jim", 56, "1955-05-09 13:12:45"),
                ("fred", 100, "1911-09-12 01:01:01")]
        cursor.executemany('''Insert Into Friends Values (%s, %s, %s);''', rows)
        connection.commit()
finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()
"""

""" Step 6 - Update a table
try:
    # Run a query
    with connection.cursor() as cursor:
        cursor.execute("UPDATE Friends SET age = %s WHERE name = %s;",
        (106, "fred"))
        connection.commit()
finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()
"""

""" Step 7 - Update many rows
try:
    # Run a query
    with connection.cursor() as cursor:
        rows = [("Jim", "jim"),
                ("John", "john"),
                ("Fred", "fred")]
        cursor.executemany("UPDATE Friends SET name = %s WHERE name = %s;",
        rows)
        connection.commit()
finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()
"""

""" Step 8 - Delete from the Friends table
try:
    # Run a query
    with connection.cursor() as cursor:
        row = cursor.execute("Delete From Friends WHERE name = %s And age = %s;", ('Jim', 27))
        connection.commit()
finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()
"""

""" Step 9 - Delete many rows from the table
try:
    # Run a query
    with connection.cursor() as cursor:
        row = cursor.executemany("Delete From Friends WHERE name = %s;", ['Jim', 'John'])
        connection.commit()
finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()
"""

""" Step 10- Delete many values based on the length of a given list instead of hard-coding values and create the required number of format strings to use
try:
    # Run a query
    with connection.cursor() as cursor:
        list_of_names = ['Fred']

        # Prepare a string with same number of placeholders as in list_of_names
        format_strings = ','.join(['%s'] * len(list_of_names))
        
        cursor.execute(
            "DELETE FROM Friends WHERE name in ({});".format(format_strings),
            list_of_names)
        
        connection.commit()
finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()
"""
