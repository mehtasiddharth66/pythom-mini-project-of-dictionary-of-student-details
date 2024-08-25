def add_student(students):
    roll_no = input("Enter roll number: ")
    name = input("Enter name: ")
    students[roll_no] = name

def update_student(students):
    roll_no = input("Enter roll number to update: ")
    if roll_no in students:
        name = input("Enter new name: ")
        students[roll_no] = name
    else:
        print("Student not found.")

def remove_student(students):
    roll_no = input("Enter roll number to remove: ")
    if roll_no in students:
        del students[roll_no]
    else:
        print("Student not found.")

def view_students(students):
    if students:
        for roll_no, name in students.items():
            print(f"Roll No: {roll_no}, Name: {name}")
    else:
        print("No students found.")

def main():
    students = {}
    while True:
        print("\n1. Add Student\n2. Update Student\n3. Remove Student\n4. View All Students\n5. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_student(students)
        elif choice == '2':
            update_student(students)
        elif choice == '3':
            remove_student(students)
        elif choice == '4':
            view_students(students)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
