## PythonRestApi

Python Rest Api using sqlite3 as database.

## How to Configure and run
1. Clone the repo using HTTP or SSH protocal
2. Company.db : Point this file in the RestApi.py by updating the variable dataBasePath
                This file exist in databaseConfig folder
3. Naviate to python fle location and run the python file with command "python RestApi.py" 
4. Supported Methods are POST,PUT,GET and DELETE <br> 
    A. GET cal:<br> 
        &nbsp;&nbsp;&nbsp;&nbsp;http://127.0.0.1:5000/company : It displayes all the data from company table.<br> 
        &nbsp;&nbsp;&nbsp;&nbsp;http://127.0.0.1:5000/company/resource?id=<ID>" :It displayes the data which matches the argument ID<br> 
        &nbsp;&nbsp;&nbsp;&nbsp;http://127.0.0.1:5000/company/resource?name=Ramesh" :It displayes the data which matches the argument name<br> 
        &nbsp;&nbsp;&nbsp;&nbsp;http://127.0.0.1:5000/company/resource?netSalary=18000" :It displayes the data which matches the argument salary<br> 

    B. POST cal:<br> 
        &nbsp;&nbsp;&nbsp;&nbsp;http://127.0.0.1:5000/company  : It will add a new data into DB make sure unique ID is passed.<br> 
        &nbsp;&nbsp;&nbsp;&nbsp;use the below json body.<br> 
        &nbsp;&nbsp;&nbsp;&nbsp;{<br> 
        &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;"ADDRESS": "Mysore",<br> 
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"AGE": 39,<br> 
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"ID": 17,<br> 
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"NAME": "Mark",<br> 
        &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;"SALARY": 45000<br> 
        &nbsp;&nbsp;&nbsp;&nbsp;}<br> 

    C. PUT cal:<br>
        &nbsp;&nbsp;&nbsp;&nbsp;http://127.0.0.1:5000/company/update  : It will update the existing datain database.<br>
        &nbsp;&nbsp;&nbsp;&nbsp;use the below json body.<br>
        &nbsp;&nbsp;&nbsp;&nbsp;{<br> 
        &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;"ADDRESS": "Mysore",<br> 
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"AGE": 39,<br> 
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"ID": 17,<br> 
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"NAME": "Mark",<br> 
        &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;"SALARY": 46000<br> 
        &nbsp;&nbsp;&nbsp;&nbsp;}<br> 

    D. Delete cal:<br>
        &nbsp;&nbsp;&nbsp;&nbsp;http://127.0.0.1:5000/company/delete/<ID> : It will delete the row from DB where ID is passed as path variable<br>
        &nbsp;&nbsp;&nbsp;&nbsp;http://127.0.0.1:5000/company/deletebyid?id=<ID> : It will delete the row from DB where ID is passed as arguments<br>