# Student Management System
# Created by: Naina Jadhav
# Date: April 2025
# Description: A console-based Python program for managing student records using OOPs and file handling.

class Student:
    def __init__(self, roll_no, name, course):
        self.roll_no = roll_no
        self.name = name
        self.course = course

    def __str__(self):
        return f"{self.roll_no},{self.name},{self.course}"


class StudentManagementSystem:
    def __init__(self, filename="students.txt"):
        self.filename = filename

    def add_student(self):
        roll_no = input("Enter Roll No: ")
        name = input("Enter Name: ")
        course = input("Enter Course: ")

        with open(self.filename, "a") as file:
            file.write(f"{roll_no},{name},{course}\n")
        print("Student added successfully!\n")

    def view_students(self):
        try:
            with open(self.filename, "r") as file:
                data = file.readlines()
                if not data:
                    print("No student records found.\n")
                    return
                print("\n--- Student List ---")
                print("Roll No | Name | Course")
                print("-------------------------")
                for line in data:
                    roll_no, name, course = line.strip().split(",")
                    print(f"{roll_no} | {name} | {course}")
                print()
        except FileNotFoundError:
            print("No records file found.\n")

    def search_student(self):
        roll_no = input("Enter Roll No to Search: ")
        found = False
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    r, n, c = line.strip().split(",")
                    if r == roll_no:
                        print(f"\n🎓 Found Student:\nRoll No: {r}\nName: {n}\nCourse: {c}\n")
                        found = True
                        break
            if not found:
                print("Student not found.\n")
        except FileNotFoundError:
            print("No records file found.\n")

    def delete_student(self):
        roll_no = input("Enter Roll No to Delete: ")
        students = []
        found = False
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    r, n, c = line.strip().split(",")
                    if r != roll_no:
                        students.append(line)
                    else:
                        found = True

            with open(self.filename, "w") as file:
                file.writelines(students)

            if found:
                print("Student deleted successfully!\n")
            else:
                print("Student not found.\n")
        except FileNotFoundError:
            print("No records file found.\n")

    def update_student(self):
        roll_no = input("Enter Roll No to Update: ")
        students = []
        updated = False
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    r, n, c = line.strip().split(",")
                    if r == roll_no:
                        print(f"Current Name: {n}, Course: {c}")
                        new_name = input("Enter new name (leave blank to keep same): ") or n
                        new_course = input("Enter new course (leave blank to keep same): ") or c
                        students.append(f"{r},{new_name},{new_course}\n")
                        updated = True
                    else:
                        students.append(line)

            with open(self.filename, "w") as file:
                file.writelines(students)

            if updated:
                print("✏️ Student details updated successfully!\n")
            else:
                print("Student not found.\n")
        except FileNotFoundError:
            print("No records file found.\n")


# --- Main Program ---
sms = StudentManagementSystem()

while True:
    print("STUDENT MANAGEMENT SYSTEM – by Naina Jadhav")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student Details")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        sms.add_student()
    elif choice == "2":
        sms.view_students()
    elif choice == "3":
        sms.search_student()
    elif choice == "4":
        sms.update_student()
    elif choice == "5":
        sms.delete_student()
    elif choice == "6":
        print("Exiting... Goodbye! 👋")
        break
    else:
        print("Invalid choice, please try again.\n")
