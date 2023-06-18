#!/usr/bin/python3
'''The purpose of this module is to write a script that lists all states with a name starting with N (upper N) from the database'''

import sys
import MySQLdb

username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

cnx = MySQLdb.connect(user=username, passwd=password, host='localhost',
port=3306, db=database)
cursor = cnx.cursor()

query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
cursor.execute(query)

rows = cursor.fetchall()

for row in rows: 
    state_id, state_name = row
    print(state_name)

cursor.close()
cnx.close()
