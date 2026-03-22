from student_data_csv import save_student, read_students

def add_student():
    name = input("Enter name: ")
    age = input("Enter age: ")
    save_student(name, age)

def show_students():
    students = read_students()
    for s in students:
        print(s)

while True:
    print("1. Add Student")
    print("2. Show Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        show_students()
    elif choice == "3":
        break
