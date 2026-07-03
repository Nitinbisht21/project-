student = {}

while True:
    print("-------What do you wnat to do ------")
    print("1 if u want to add student")
    print("2 To view student")
    print("3 Update marks of student")
    print("4 To delete student")
    print("5 To rename student")
    print("6 To exit")

    choice = input("Enter the choice: ")

    if choice == '1':
        name = input("Enter the name of student: ")
        marks = input("Enter the marks of student: ")
        student[name] = marks
        print("Student added successfully")
    
    elif choice == '2':
        if student:
            for name, marks in student.items():
                print(f"Name: {name}, Marks: {marks}")
        else:
            print("No students found.")

    elif choice == '3':
        name = input("Enter the name of student to update marks: ")
        if name in student:
            marks = input("Enter the new marks: ")
            student[name] = marks
            print("Marks updated successfully.")
        else:
            print("Student not found.")

    elif choice == '4':
        name = input("Enter the name of student to delete: ")
        if name in student:
            del student[name]
            print("Student deleted successfully.")
        else:
            print("Student not found.")

    elif choice == '5':
        old_name = input("Enter the current name of the student: ")
        if old_name in student:
            new_name = input("Enter the new name for the student: ")
            student[new_name] = student[old_name]
            del student[old_name]
            print("Student renamed successfully.")
        else:
            print("Student not found.")

    elif choice == '6':
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")