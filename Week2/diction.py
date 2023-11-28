student_database = {}

def AddStudent():
    name = input("Input student's name: ")
    age = input("Input student's age: ")
    grade = input("Input student's grade: ")

    student_database[name] = {"Age": age, "Grade": grade}

def ViewStudent():
    name = input("Input student's name: ")
    if name in student_database:
        print("Viewing Student Details")
        print("Name: " + name)
        print("Age: " + student_database[name]["Age"])
        print("Grade: " + student_database[name]["Grade"])
    else:
        print("Not found")

def ListAllStudents():
    if student_database:
        print("List of All Students")
        for name, details in student_database.items():
            print("Name: ", name)
            print("Age: ", details["Age"])
            print("Grade", details["Grade"])
            print("============================")
    else:
        print("There are no students")

def UpdateStudent():
    name = input("Input name: ")
    if name in student_database:
        age = input("Input updated age: ")
        grade = input("Input updated grade: ")

        student_database[name]["Age"] = age
        student_database[name]["Grade"] = grade

    else: 
        print("No such student")

def DeleteStudent():
    name = input("Input student's name: ")
    if name in student_database:
        del student_database[name]
    else:
        print("No such student")


while True:
    print("1. Add Student")
    print("2. View Student")
    print("3. List All Students")
    print("4. Update Student Information")
    print("5. Delete Student")
    print("6. Quit")

    choose = input("Choose 1-5: ")

    match choose:
        case "1":
            AddStudent()
        case "2":
            ViewStudent()
        case "3":
            ListAllStudents()
        case "4":
            UpdateStudent()
        case "5":
            DeleteStudent()
        case "6":
            break
        case _:
            print("Please choose 1-5")