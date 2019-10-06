#!/usr/bin/env python3
# encoding=utf-8
import mysql.connector as mc
import sys

database = sys.argv[1]
table = sys.argv[2]
print(type(table))
print(table)
# SQL = (
# '''
# SELECT * FROM %s
# '''
# )
QUERY = 'SELECT * FROM app'
# works this way
SQL = ('''SELECT * FROM %s''' % table)
dbconfig = {
        'host': '127.0.0.1',
        'user': 'root',
        'password': 'mj199207',
        'database': database,
        }
conn = mc.connect(**dbconfig)
cursor = conn.cursor()
# use a tuple to replace placeholders(%s) in prepared statement
# cursor.execute(SQL, (table,))
cursor.execute(SQL)
# cursor.execute(SQL)
# conn.commit()
# use commit() to UPDATE, not SELECT

res = cursor.fetchall()
for line in res:
    print(line)
cursor.close()
conn.close()
