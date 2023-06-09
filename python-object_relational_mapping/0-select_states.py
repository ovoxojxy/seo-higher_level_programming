#!/usr/bin/python3
'''This module writes a script that lists all states frm the database hbt                                                                          
n_e_0_usa using 3 arguments and sorting in ascending order by states '''


import sys
import MySQLdb




#get commandd line arguemtns'''
username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

#establish database connection'''
cnx = MySQLdb.connect(user=username, passwd=password,
host='localhost', port=3306, db=database)
cursor = cnx.cursor()


#execute the query to fetch all cities'''
query = 'SELECT * FROM states ORDER BY id ASC'
cursor.execute(query)

#fetch all the rows'''
rows = cursor.fetchall()

for row in rows:
    #iterate over the rows and print city names'''
    state_id, state_name = row
    print(state_name)

#close cursor and database connection'''
cursor.close()
cnx.close()
