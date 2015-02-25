#!/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2
import sys
import csv

con_string =  "dbname='food_truck' user='aabulota' password='dinotruck'"

con = psycopg2.connect(con_string)
cursor = con.cursor()

try:
    con = psycopg2.connect(con_string)
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS locations")

cur.execute("CREATE TABLE locations (id SERIAL PRIMARY KEY, truck_id INT FOREIGN KEY REFERENCES trucks(id), day TEXT, start_time TIME WITHOUT TIME ZONE, end_time TIME WITHOUT TIME ZONE, address TEXT, neighborhood TEXT)")

except:
    print "Unable to connect to database"

# locations = open("scraped_dynamic.csv", "r")

# first_line = locations.readline()

# for location in locations:

#     locList = location.split( ',')
#     dayofweek = locList[0]
#     start = locList[1]
#     end = locList[2]
#     add = locList[3]
#     neigh = locList[4]

#     query = "INSERT INTO locations (day, start_time, end_time, address, neighborhood) VALUES (%s, %s, %s, %s, %s);"
#     try:
#         cur.execute(query, dayofweek, start, end, add, neigh))
#     except Exception as e:
#         print e
#         print "%s %s %s %s %s" % (dayofweek, start, end, add, neigh)
#         print "Unable to print %s." % (query, )
#         print e

con.commit()
con.close()

