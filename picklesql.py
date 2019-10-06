#!/usr/bin/env python3
# encoding=utf-8
import pickle
import mysql.connector

dbconfig = {
        'host' : '127.0.0.1',
        'user' : 'root',
        'password' : 'mj199207',
        'database' : 'pickle'
        }
conn = mysql.connector.connect(**dbconfig)
cursor = conn.cursor()
SQL = '''
CREATE TABLE %(
id INT PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(20) NOT NULL,
val VARCHAR(50) NOT NULL);
'''
INSERT = '''
INSERT INTO % 
VALUES(%, %, %);
'''
cursor.execute(SQL, 'list')
cursor.execute(SQL, 'set')
cursor.execute(SQL, 'dict')
cursor.execute(SQL, 'tuple')
