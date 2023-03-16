import db
from pprint import pprint


def interatc():
    option = input('''Pick from following option:
                   1. Display
                   2. Insert
                   3. Update
                   4. Delete    ''')
    if option == "Display":
        table_name = input("enter table name: ")
        result = db.display(table_name)
        for row in result:
            print(row, '\n')
    if option == "Insert":
        id = input("enter student id: ")
        name = input("enter student name: ")
        department = input('''enter department name: it should be from the list:
                           Biology
                            Comp. Sci.
                            Elec. Eng.
                            Finance
                            History
                            Music
                            Physics''')
        credits = input("enter no.of tot_creds: ")
        result = db.insert(int(id), name, department, credits)
        print('row inserted at : '+ str(result))
    if option == "Update":
        student_name = input("enter student name: ")
        result = db.get_instructor(student_name)
        if result is not None:
            for row in result:
                print("instructor for the student is : "+ row[0])

        result = db.get_instructors()
        instructors = []
        print("all available instructors")
        for row in result:
            instructors.append(row[0])
            #print("\n ", row[0])
        pprint(instructors)
        result = db.get_students()
        students = []
        print("all available students")
        for row in result:
            students.append(row[0])
            #print("\n ", row[0])
        pprint(students)
        instructor_name = input("pick a instructor from above to assosiate a Student: ")
        student_name = input("pick a student from above to assosiate a instructor: ")
        db.update(student_name,instructor_name)
    if option == "Delete":
        student_name = input("enter student name: ")
        result = db.get_record(student_name)
        if result is not None:
            confirm = input('Are you sure you want to delete Y or N:')
            if confirm == 'Y':
                delete = db.delete(student_name)
                print('student go deleted')
    else:
        print("Exit")

if __name__ == "__main__":
    interatc()