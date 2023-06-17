#!/usr/bin/python3
''' This modules purpose is to Write a script that lists all cities from the database hbtn_0e_4_usa'''
''' Documentation documentation documentation documentation documentation documentation '''


import sys
import MySQLdb


username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

cnx = MySQLdb.connect(user=username, passwd=password, host='localhost', port=3306, db=database)
cursor = cnx.cursor()

query = "SELECT * FROM cities ORDER BY id ASC"
cursor.execute(query)

rows = cursor.fetchall()

for row in rows:
    city_id, city_name, state_id = row
    print(city_name)

cursor.close()
cnx.close()
