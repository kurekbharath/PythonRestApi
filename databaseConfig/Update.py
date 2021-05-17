#!/usr/bin/env python

import sqlite3

dataBasePath = "C:/Bharath/DevOps/poc/mypython/sqlite/Tables"
databaseName = "Company.db"

conn = sqlite3.connect(dataBasePath + "/" + databaseName)
conn.execute("UPDATE COMPANY set salary=25000 where id=1")
conn.commit()

cursor = conn.execute("SELECT * from COMPANY")
for row in cursor:
    print("ID: ", row[0])
    print("Name: ", row[1])
    print("Age: ", row[2])
    print("Address: ", row[3])
    print("Salary: ", row[4],"\n")

print ("UPDATE Operation done successfully")
conn.close()