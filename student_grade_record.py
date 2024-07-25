students = { }
def add_student(name, grade):
    students[name] = grade
    print(f"{name} added with grade {grade}")

def update_student(name, grade):
    if name in students:
        students[name] = grade
        print(f"{name} updated with grade {grade}")
    else:
        print(f"{name} is not found in record")

def delete_student(name):
    if name in students:
        del students[name]
        print(f"{name} has been deleted successfully")
    else:
        print(f"{name} is not found in record.")

def display_students():
    for name, grade in students.items():
        print(f"{name} :    {grade}")
        print("--------------------")


def main():
    while True:
        print("1 : Add record")
        print("2 : Update record")
        print("3 : Delete record")
        print("4 : Display record")
        print("5 : Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            name = input("Enter the name of the student: ")
            grade = input("Enter the grade of the student: ")
            add_student(name, grade)

        elif choice == 2:
            name = input("Enter the name of the student: ")
            grade = input("Enter the grade of the student: ")
            update_student(name, grade)

        elif choice == 3:
            name = input("Enter the name of the student you want to delete: ")
            delete_student(name)

        elif choice == 4:
            display_students()

        elif choice == 5:
            print("Record is closing")
            break
        else:
            print("Invalid Choice")
main()


