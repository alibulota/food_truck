#!/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2
import csv
import sys



con_string =  "dbname='food_truck' user='aabulota'"

con = psycopg2.connect(con_string)
cursor = con.cursor()

try:
    con = psycopg2.connect(con_string)
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS trucks")
        # Make sure to check if the table exists - what we really want to do is ONLY create it if it doesn't exist
        # Maybe verify the schema if t already exists against what we expect?
    cur.execute("CREATE TABLE trucks(id SERIAL PRIMARY KEY, name TEXT, website TEXT, cuisine TEXT, payment TEXT, twitter TEXT)")

except:
    print "Unable to connect to connect/create table"

# No real point
# try:
#     cur.execute("SELECT * FROM trucks")

# except:
#     print "Unable to SELECT from trucks"


trucks = open("scraped_static.csv", "r")

# skip reading the first line by reading it here instead
first_line = trucks.readline()

for truck in trucks:

    truckList = truck.split( ',')
    name = truckList[1]
    site = truckList[2]
    food = truckList[3]
    pay = truckList[4]
    twit = truckList[5]

    # Should make sure these entries don't already exist
    query = "INSERT INTO trucks(name, website, cuisine, payment, twitter) VALUES (%s, %s, %s, %s, %s);" 
    try:
        cur.execute(query, (name, site, food, pay, twit))
    except Exception as e:
        # Important to print / log errors!
        print e
        print "%s %s %s %s %s" % (name, site, food, pay, twit)
        print "Unable to print %s." % (query, )
        # Crash early if we get an exception - our data is bad!
        raise e

    

# Make sure we actually commit our changes and close the connection
con.commit()
con.close()
