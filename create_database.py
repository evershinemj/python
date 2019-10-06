#!/usr/bin/env python3
# encoding=utf-8
import mysql.connector as mc
import sys

dbconfig = {
        'host': '127.0.0.1',
        'user': 'root',
        'password': 'mj199207',
        }
database = sys.argv[1]
conn = mc.connect(**dbconfig)
cursor = conn.cursor()
SQL = 'CREATE DATABASE %s;' % database
cursor.execute(SQL)
