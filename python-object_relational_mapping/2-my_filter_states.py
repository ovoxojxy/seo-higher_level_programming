#!/usr/bin/python3
'''This module writes a script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument'''

import sys
import MySQLdb

username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]
state_name = sys.argv[4]

cnx = MySQLdb.connect(user=username, passwd=password, host='localhost',
port=3306, db=database)
cursor = cnx.cursor()

query = "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC"
cursor.execute(query, (state_name,))

rows = cursor.fetchall()

for row in rows:
    state_id, state_name = row
    print(state_name)

cursor.close()
cnx.close()
