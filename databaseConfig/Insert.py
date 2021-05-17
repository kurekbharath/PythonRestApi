#!/usr/bin/env python

import sqlite3

dataBasePath = "C:/Bharath/DevOps/poc/mypython/sqlite/Tables"
databaseName = "Company.db"

#Insert opeation
conn = sqlite3.connect(dataBasePath + "/" + databaseName)

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
                VALUES(5,'John',32,'Texas',25000)")

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
                VALUES(6,'Mark',36,'Denmark',25000)")

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
                VALUES(7,'George',38,'Athens',18000)")

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
                VALUES(8,'Matthew',40,'Chicao',18000)")
conn.commit()
print ("INSERT Operation done successfully")
conn.close()