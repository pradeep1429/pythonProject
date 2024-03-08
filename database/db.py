import sqlite3


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

connection.commit()
connection.close()