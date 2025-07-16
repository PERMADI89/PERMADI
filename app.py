import streamlit as st
from auth import check_login
from dashboard import show_dashboard
from database import init_db, insert_data, fetch_all

st.set_page_config(page_title="Admin Dashboard", layout="wide")

# Inisialisasi database
init_db()

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("🔐 Admin Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if check_login(username, password):
            st.session_state.logged_in = True
            st.success("Login berhasil!")
        else:
            st.error("Username atau password salah.")
else:
    st.sidebar.title("📁 Menu")
    menu = st.sidebar.radio("Navigasi", ["📊 Dashboard", "➕ Tambah Data", "📑 Lihat Data", "🔓 Logout"])

    if menu == "📊 Dashboard":
        show_dashboard()
    elif menu == "➕ Tambah Data":
        st.header("➕ Tambah Data Karyawan")
        with st.form("form"):
            name = st.text_input("Nama Lengkap")
            email = st.text_input("Email")
            umur = st.number_input("Umur", min_value=1, max_value=100)
            divisi = st.selectbox("Divisi", ["IT", "HR", "Finance", "Marketing"])
            submitted = st.form_submit_button("Simpan")
            if submitted and name and email:
                insert_data(name, email, umur, divisi)
                st.success("Data berhasil ditambahkan!")
    elif menu == "📑 Lihat Data":
        st.header("📑 Data Karyawan")
        data = fetch_all()
        st.dataframe(data)
    elif menu == "🔓 Logout":
        st.session_state.logged_in = False
        st.experimental_rerun()
