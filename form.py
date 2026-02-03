import streamlit as st
import mysql.connector

# ✅ Database connection
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Ganga@1407_",  # your MySQL password
        database="form_db"       # your database name
    )

# ✅ Register new user
def register_user(name, password, email):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO users (name, password, email) VALUES (%s, %s, %s)",
            (name, password, email)
        )
        conn.commit()
        st.success("Registration successful! You can now log in.")
    except mysql.connector.Error as err:
        st.error(f"Error: {err}")
    finally:
        conn.close()

# ✅ Login check
def login_user(name, password):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM users WHERE name=%s AND password=%s",
        (name, password)
    )
    result = cursor.fetchone()
    conn.close()
    return result

# 🎨 Streamlit UI
st.title("Login & Registration System")

menu = ["Login", "Register"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Register":
    st.subheader("Create New Account")
    name = st.text_input("Name")
    password = st.text_input("Password", type="password")
    email = st.text_input("Email")
    if st.button("Register"):
        if name and password and email:
            register_user(name, password, email)
        else:
            st.error("Please fill all fields.")

elif choice == "Login":
    st.subheader("Login to Your Account")
    name = st.text_input("Name")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        user = login_user(name, password)   # ✅ use 'name'
        if user:
            st.success(f"Welcome {name}!")
            st.write("You are now logged in.")
        else:
            st.error("Invalid name or password")