#!/usr/bin/python3
'''This module writes a script that lists all states frm the database hbt                                                                          
n_e_0_usa using 3 arguments and sorting in ascending order by states '''


import sys
import MySQLdb


'''This module writes a script that lists all states frm the database hbt                                                                          
n_e_0_usa using 3 arguments and sorting in ascending order by states '''


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
