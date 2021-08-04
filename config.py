import pymysql

"""
connection to mySql
"""

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    db="auto_complete_data",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)
