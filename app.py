import streamlit as st
from database import create_login_table, add_user_login, login_user

# Inisialisasi database login
create_login_table()

st.set_page_config(page_title="Admin Login", layout="centered", page_icon="🔐")

if 'login_status' not in st.session_state:
    st.session_state.login_status = False

menu = st.sidebar.selectbox("Menu", ["Login", "Tambah User"])

if menu == "Login":
    st.markdown("## 🔐 Admin Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if login_user(username, password):
            st.success("Login berhasil!")
            st.session_state.login_status = True
            st.rerun()
        else:
            st.error("Login gagal. Cek kembali username dan password.")

elif menu == "Tambah User":
    st.markdown("## ➕ Tambah User Login")
    new_user = st.text_input("Username Baru")
    new_pass = st.text_input("Password", type="password")
    if st.button("Tambah"):
        if new_user and new_pass:
            if add_user_login(new_user, new_pass):
                st.success(f"User '{new_user}' berhasil ditambahkan.")
            else:
                st.warning("Username sudah terdaftar.")
        else:
            st.warning("Mohon isi semua kolom.")
