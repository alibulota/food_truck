#!/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2
import csv
import sys


con_string =  "dbname='food_truck' user='aabulota' password='dinotruck'"

con = psycopg2.connect(con_string)
cursor = con.cursor()

try:
    con = psycopg2.connect(con_string)
    cur = con.cursor()
    cur.execute("CREATE TABLE trucks (Id INTEGER PRIMARY KEY, trucks TEXT, website TEXT, payment TEXT, twitter TEXT)")

except:
    print "Unable to connect to database"

try:
    cur.execute("SELECT * FROM trucks")

except:
    print "Unable to SELECT from trucks"


trucks = open("scraped_info.csv", "r")

# skip reading the first line by reading it here instead
first_line = trucks.readline()

for truck in trucks:

    truckList = truck.split( ',')
    name = truckList[1]
    site = truckList[2]
    food = truckList[3]
    pay = truckList[4]
    twit = truckList[5]

    query = "INSERT INTO trucks (trucks, website, food_type, payment, twitter) VALUES (%s, %s, %s, %s, %s);" 
    try:
        cur.execute(query, (name, site, food, pay, twit))
    except:
        print "Unable to print %s." % (query,)


