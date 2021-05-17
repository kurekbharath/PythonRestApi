#!/usr/bin/env python

import sqlite3

dataBasePath = "C:/Bharath/DevOps/poc/mypython/sqlite/Tables"
databaseName = "Company.db"

conn = sqlite3.connect(dataBasePath + "/" + databaseName)
conn.execute("DELETE from COMPANY where id=4")
print("Total Changes ",  conn.total_changes, "\n")
conn.close

cursor = conn.execute("SELECT id, name, age, address, salary from COMPANY")
for row in cursor:
    print("ID: ", row[0])
    print("Name: ", row[1])
    print("Age: ", row[2])
    print("Address: ", row[3])
    print("Salary: ", row[4],"\n")

print ("DELETE Operation done successfully")
conn.close()