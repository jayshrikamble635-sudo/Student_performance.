import streamlit as st
import csv

st.title("Student Management System")

# Function to save data
def save_student(name, age):
    with open("students.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, age])

# Function to read data
def read_students():
    students = []
    try:
        with open("students.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                students.append(row)
    except:
        pass
    return students

# Input fields
name = st.text_input("Enter Name")
age = st.text_input("Enter Age")

if st.button("Add Student"):
    save_student(name, age)
    st.success("Student Added!")

if st.button("Show Students"):
    data = read_students()
    for student in data:
        st.write(student)
