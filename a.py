"""import streamlit as st
st.title("Hello, Streamlit!")
a=st.number_input("Enter a number:", value=0)
if st.button("ok"):
    st.success(f"You entered: {a}")
else:
    st.warning("Please enter a number and click ok.")"""""
#pip install mysql-connector-python
import streamlit as st
import mysql.connector

# ✅ Database connection function
def get_connection():
    return mysql.connector.connect(
        host="localhost",       # change if needed
        user="root",            # your MySQL username
        password="Ganga@1407_", # your MySQL password
        database="db1"          # your database name
    )

# ✅ Create operation
def create_student(names, marks, emails):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO students (names, marks, emails) VALUES (%s, %s, %s)",
        (names, marks, emails)
    )
    conn.commit()
    conn.close()

# ✅ Read operation
def read_student():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()
    return rows

# ✅ Update operation
def update_student(student_id, names, marks, emails):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE students SET names=%s, marks=%s, emails=%s WHERE id=%s",
        (names, marks, emails, student_id)
    )
    conn.commit()
    conn.close()

# ✅ Delete operation
def delete_student(student_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id=%s", (student_id,))
    conn.commit()
    conn.close()

# 🎨 Streamlit UI
st.title("MySQL CRUD App with Streamlit")

menu = ["Create", "Read", "Update", "Delete"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Create":
    st.subheader("Add New Student")
    names = st.text_input("Name")
    marks = st.number_input("Marks", min_value=0)
    emails = st.text_input("Email")
    if st.button("Add Student"):
        create_student(names, marks, emails)
        st.success(f"Student {names} added successfully!")

elif choice == "Read":
    st.subheader("View Students")
    students = read_student()
    for s in students:
        st.write(f"ID: {s[0]}, Name: {s[1]}, Marks: {s[2]}, Email: {s[3]}")

elif choice == "Update":
    st.subheader("Update Student")
    student_id = st.number_input("Student ID", min_value=1)
    names = st.text_input("New Name")
    marks = st.number_input("New Marks", min_value=0)
    emails = st.text_input("New Email")
    if st.button("Update Student"):
        update_students(student_id, names, marks, emails)
        st.success(f"Student ID {student_id} updated successfully!")
elif choice == "Delete":
    st.subheader("Delete Student")
    student_id = st.number_input("Student ID to Delete", min_value=1)
    if st.button("Delete Student"):
        delete_student(student_id)
        st.success(f"Student ID {student_id} deleted successfully!")


