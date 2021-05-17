#!/usr/bin/env python

import sqlite3

dataBasePath = "C:/Bharath/DevOps/poc/mypython/sqlite/Tables"
databaseName = "Company.db"

conn = sqlite3.connect(dataBasePath + "/" + databaseName)

cursor = conn.execute("Select * FROM COMPANY").fetchall()
print(cursor)
for cur in cursor:
    print("ID: ", cur[0])
    print("Name: ", cur[1])
    print("Age: ", cur[2])
    print("Address: ", cur[3])
    print("Salary: ", cur[4],"\n")

print("SELECT Operation are successfull")
conn.close()