import sqlite3

import pandas as pd
import requests

connection = sqlite3.connect('C:\\Users\\Pradeep_Avadhanam\\AppData\\Local\\DBeaver\\sqllite\\hello.sqllite')
cursor = connection.cursor()
query = ("select j.job_title from jobs j where j.job_id in("
         + "select e.job_id from employees e where e.department_id=("
         +"select d.department_id from departments d where d.department_name = 'Sales'))"
         +" UNION select j.job_title from jobs j where j.job_id in("
         +"select e.job_id from employees e where e.department_id=("
         +"select d.department_id from departments d where d.department_name = 'Accounting'))")
query = "select d.department_id,e.first_name,e.salary from departments d inner join employees e on e.department_id = d.department_id where e.department_id = 10 and e.salary > 8000"

cursor.execute(query)
rows = cursor.fetchall()
for row in rows:
    print(row, type(row))
    print(row[2:3])




api_json = requests.get("https://reqres.in/api/products/2")
api_data = api_json.text
print(api_data)
api_df = pd.read_json(api_data)
print(api_df.support['url'])

db_df = pd.read_sql(query,connection)
print(db_df.head())

api_df = api_df.astype(str).apply(lambda x: x.str.lower())
db_df = db_df.astype(str).apply(lambda x: x.str.lower())
print(api_df)
print(db_df)
connection.commit()
connection.close()