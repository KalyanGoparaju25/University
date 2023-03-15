import datetime
import mysql.connector

def display(table_name:str):
    print('this is display mode for table '+ table_name)
    cnx = mysql.connector.connect(user='root',password='1234', database='university')
    cursor = cnx.cursor(buffered=True)
    print("got cursor")
    query = ("SELECT * FROM "+ table_name)
    cursor.execute(query)
    rows = cursor.fetchall()

    cursor.close()
    cnx.close()

    return rows

def insert(id:int, name:str, department:str, credits:str):
     cnx = mysql.connector.connect(user='root',password='1234', database='university')
     cursor = cnx.cursor(buffered=True)
     print("got cursor")
     query = ("INSERT INTO STUDENT(ID, name, dept_name, tot_cred) VALUES(%s,%s,%s,%s) ")
     val = (id, name, department, credits)
     cursor.execute(query, val)
     
     cnx.commit()
     cursor.close()
     cnx.close()
     return cursor.rowcount
def update(student_name:str, instructor_name:str):
    print('this is update mode')
    cnx = mysql.connector.connect(user='root',password='1234', database='university')
    cursor = cnx.cursor(buffered=True)
   
    student_query = ("select ID from STUDENT where name = '"+student_name+"'")
    cursor.execute(student_query)
    result = cursor.fetchall()
    student_id=''
    for row in result:
        student_id = row[0]
        print(student_id)

    instructor_query = ("select ID from INSTRUCTOR where name = '"+instructor_name+"'")
    cursor.execute(instructor_query)
    result = cursor.fetchall()
    instructor_id = ''
    for row in result:
        instructor_id = row[0]
        print( instructor_id)
    query = ("INSERT INTO ADVISOR(s_ID, i_ID) VALUES(%s,%s)  ON DUPLICATE KEY UPDATE s_ID=%s")
    
    val = (student_id, instructor_id, student_id)
    cursor.execute(query, val)
     
    cnx.commit()
    cursor.close()
    cnx.close()
    return cursor.rowcount
def get_instructor(student_name: str):
    cnx = mysql.connector.connect(user='root',password='1234', database='university')
    cursor = cnx.cursor(buffered=True)
    
    query = ("select name from INSTRUCTOR I INNER JOIN ADVISOR A ON I.ID = A.i_ID where A.s_ID = (select ID from STUDENT where name = '"+student_name+"')")

    cursor.execute(query)
    result = cursor.fetchall()

    cursor.close()
    cnx.close()
    return result

def get_instructors():
    cnx = mysql.connector.connect(user='root',password='1234', database='university')
    cursor = cnx.cursor(buffered=True)
    
    query = ("select name from INSTRUCTOR ")

    cursor.execute(query)
    result = cursor.fetchall()

    cursor.close()
    cnx.close()
    return result
   
def get_students():
    cnx = mysql.connector.connect(user='root',password='1234', database='university')
    cursor = cnx.cursor(buffered=True)
    
    query = ("select name from STUDENT ")

    cursor.execute(query)
    result = cursor.fetchall()

    cursor.close()
    cnx.close()
    return result
   
def get_record(student_name:str):
    
    cnx = mysql.connector.connect(user='root',password='1234', database='university')
    cursor = cnx.cursor(buffered=True)
    
    query = ("SELECT * FROM STUDENT WHERE name = '"+ student_name+"'")
    
    cursor.execute(query)
    result = cursor.fetchall()

    cursor.close()
    cnx.close()
    return result

def delete(student_id:str):
    
    cnx = mysql.connector.connect(user='root',password='1234', database='university')
    cursor = cnx.cursor(buffered=True)
    
    query = ("delete FROM STUDENT WHERE name = '"+student_id+"'")
    
    print(query)
    cursor.execute(query)
    cnx.commit()

    cursor.close()
    cnx.close()
    return cursor.rowcount
