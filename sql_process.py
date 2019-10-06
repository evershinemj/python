#!/usr/bin/env python3
# encoding=utf-8
import mysql.connector as mc
import sys

database = sys.argv[1]
SQL = sys.argv[2]
dbconfig = {
        'host': '127.0.0.1',
        'user': 'root',
        'password': 'mj199207',
        'database': database,
        }
conn = mc.connect(**dbconfig)
cursor = conn.cursor()
# SQL = 'CREATE TABLE %s(id INT PRIMARY KEY AUTO_INCREMENT);' % table
cursor.execute(SQL)
if SQL.upper().startswith('SHOW') or SQL.upper().startswith('SELECT'):
    # read results to prevent Exception
    for row in cursor.fetchall():
        print(row)
    pass
else:
    conn.commit()
cursor.close()
conn.close()
