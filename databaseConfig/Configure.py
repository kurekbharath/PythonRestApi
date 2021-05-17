#!/usr/bin/env python
import os
import sys
import sqlite3

dataBasePath = "C:/Bharath/DevOps/poc/mypython/sqlite/Tables"
databaseName = "Company.db"

try:
    if os.path.isfile(dataBasePath + "/" + databaseName):
        print("Database already exist: " + databaseName)
    else:
        print("Creating a new database: " + databaseName)
        conn = sqlite3.connect(dataBasePath + "/" + databaseName)
        print ("Opened database successfully : "+ databaseName)
        conn.execute(''' CREATE TABLE COMPANY
                        (   ID INT PRIMARY KEY NOT NULL,
                            NAME TEXT NOT NULL,
                            AGE  INT  NOT NULL,
                            ADDRESS CHAR(50),
                            SALARY REAL
                        );
                    ''')
        print("Table created with the name COMPANY")
except:
    print("Database configuration failed error detail are ", sys.exc_info())

