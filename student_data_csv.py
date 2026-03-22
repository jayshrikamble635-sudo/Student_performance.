import csv

def save_student(name, age):
    with open("students.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, age])

def read_students():
    students = []
    try:
        with open("students.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                students.append(row)
    except FileNotFoundError:
        print("No data found")
    return students
