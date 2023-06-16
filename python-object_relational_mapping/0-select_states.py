#!/usr/bin/python3
'''this module writes a script that lists all
states from the database hbtn_0e_0_usa'''


import sys
import MySQLdb

username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

cnx = MySQLdb.connect(user=username, passwd=password,
host='localhost', port=3306, db=database)
cursor = cnx.cursor()

query = 'SELECT * FROM states ORDER BY id ASC'
cursor.execute(query)

rows = cursor.fetchall()


for row in rows:
    state_id, state_name = row
    print(state_name)

cursor.close()
cnx.close()
