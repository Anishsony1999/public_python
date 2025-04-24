# step1 : pip install mysql-connector-python
# step2 : import mysql.connector
# step3 : create connection
#   host = "localhost", user = "root", password = "",name = "py"

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost", # hostname
    user = "root",  # username
    password = "root", # password if you have otherwaise ""
    name = "py" # database name
)

mycursor = mydb.cursor() # create a cursor object

mycursor.execute("select * from student_products")

for i in mycursor:
    print(i)
