import streamlit as st
from student_data_csv import save_student, read_students

st.title("Student Management System")

menu = st.sidebar.selectbox("Menu", ["Add Student", "View Students"])

if menu == "Add Student":
    st.subheader("Add New Student")
    
    name = st.text_input("Enter Name")
    age = st.text_input("Enter Age")

    if st.button("Add"):
        if name and age:
            save_student(name, age)
            st.success("Student Added Successfully")
        else:
            st.warning("Please fill all fields")

elif menu == "View Students":
    st.subheader("Student List")
    
    students = read_students()
    
    if students:
        for s in students:
            st.write("Name:", s[0], "Age:", s[1])
    else:
        st.write("No student data found")
