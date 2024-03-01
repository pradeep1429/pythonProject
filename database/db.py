import sqlite3


connection = sqlite3.connect('C:\\Users\\Pradeep_Avadhanam\\AppData\\Local\\DBeaver\\sqllite\\hello.sqllite')
cursor = connection.cursor()
query = ("select j.job_title from jobs j where j.job_id in("
         + "select e.job_id from employees e where e.department_id=("
         +"select d.department_id from departments d where d.department_name = 'Sales'))"
         +" UNION select j.job_title from jobs j where j.job_id in("
         +"select e.job_id from employees e where e.department_id=("
         +"select d.department_id from departments d where d.department_name = 'Accounting'))")

cursor.execute(query)
rows = cursor.fetchall()
for row in rows:
    print(row, type(row))

connection.commit()
connection.close()