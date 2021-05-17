#!/usr/bin/env python

import flask
from flask import request, jsonify
import sqlite3

app = flask.Flask(__name__)
app.config["DEBUG"] == True

dataBasePath = "./databaseConfig"
databaseName = "Company.db"

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

#404 error handling
@app.errorhandler(404)
def notFound(error=None):
   message = {
       'status': 404,
       'message': 'Not Found:' + request.url,
   }
   respone = jsonify(message)
   respone.status_code =404

#Get api to fetch all the details
@app.route("/company",methods=["GET"])
def getCompanyDetails():

    conn= sqlite3.connect(dataBasePath + "/" + databaseName)
    conn.row_factory = dict_factory
    cur = conn.cursor()
    companyDetails = cur.execute('select * from Company').fetchall()

    return jsonify(companyDetails)

#GET api WRT ID or Name or netsalary
@app.route("/company/resource",methods=["GET"])
def getResourceDetails():
    try:
        parameters = request.args
        id = parameters.get('id')
        name = parameters.get('name')
        netSalary = parameters.get('netSalary')
        query = "select * from COMPANY where "
        filter = []
        if id:
            query += "ID=? AND"
            filter.append(id)
        elif name:
            query += "name=? AND"
            filter.append(name)
        elif netSalary:
            query += "salary=? AND"
            filter.append(netSalary)
        elif not (id or name):
            return notFound()

        query = query[:-4] + ";"   

        conn= sqlite3.connect(dataBasePath + "/" + databaseName)
        conn.row_factory = dict_factory
        cur = conn.cursor()
        query = cur.execute(query,filter).fetchall()

        return jsonify(query)
    except Exception as e:
        return "Get cal exception ", e
    finally:
        conn.close()
#Post cal to update the employee data
@app.route("/company",methods=["POST"])
def getDetailsByAttributes():

    json    = request.json
    ID      = json['ID']
    NAME    = json['NAME']
    AGE     = json['AGE'] 
    ADDRESS = json['ADDRESS']
    SALARY  = json['SALARY']
    
    if ID and NAME and AGE and ADDRESS and SALARY and request.method == 'POST':
        
        query = ''' INSERT INTO company 
                    (ID, NAME, AGE, ADDRESS, SALARY)
                     VALUES (?,?,?,?,?)
        '''
        data = (ID, NAME, AGE, ADDRESS, SALARY)

        conn= sqlite3.connect(dataBasePath + "/" + databaseName)
        cursor = conn.cursor()
        cursor.execute(query,(data))
        conn.commit() 
        response = jsonify('{Message: Data has been inserted successfully}')
        response.status_code = 200
        return response
    else:
         return "Please check the data passed", 404

#update the existing employee data
@app.route("/company/update",methods=["PUT"])
def updateEmployeeDetails():
    inputData = request.json
    id      = inputData['ID']
    name    = inputData['NAME']
    age     = inputData['AGE']
    address = inputData['ADDRESS']
    salary  = inputData['SALARY']

    if id and name and age and address and salary and request.method == 'PUT':
        query = ''' update company set name=?,age=?,address=?,salary=? where id=?'''
        data = (name,age,address,salary,id)

        conn = sqlite3.connect(dataBasePath + "/" + databaseName)
        cursor = conn.cursor()
        cursor.execute(query,data)
        conn.commit()
        conn.close()
        response = jsonify('{Message: Data has been Updated successfully}')
        response.status_code == 201
        return response
    else:
        return "Please check the data passed", 404

#delete by argument
@app.route("/company/deletebyid", methods=["DELETE"])
def deleteByID():
    try:
        parameters = request.args
        id = parameters.get('id')
        
        query = ''' DELETE FROM company where id=? '''
        filter = []
        filter.append(id)
        
        conn = sqlite3.connect(dataBasePath + "/" + databaseName)
        cursor = conn.cursor()
        cursor.execute(query,filter)
        conn.commit()
        response = jsonify ('{Message: Data has been deleted}')
        response.status_code == 204
        return response
    except Exception as e:
        print("Exception block: " + str(e))
        return e
    finally:
        cursor.close() 
        conn.close()

#Delete by path
@app.route('/company/delete/<int:id>', methods=['DELETE'])
def delete_emp(id):
    try:
    
        conn = sqlite3.connect(dataBasePath + "/" + databaseName)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM company WHERE id =%d" %id)
        conn.commit()
        respone = jsonify('Employee deleted successfully!')
        respone.status_code = 200
    
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()
		
app.run()