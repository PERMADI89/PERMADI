import streamlit as st
from auth import check_login
from dashboard import show_dashboard
from database import init_db, insert_data, fetch_all
import pandas as pd

st.set_page_config(page_title="Admin Dashboard Extended", layout="wide")

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
    menu = st.sidebar.radio("Navigasi", [
        "📊 Dashboard", 
        "➕ Tambah Data", 
        "📑 Lihat Data", 
        "📈 Lihat Data Rekap", 
        "🔓 Logout"
    ])

    if menu == "📊 Dashboard":
        show_dashboard()
    elif menu == "➕ Tambah Data":
        st.header("➕ Tambah Data Aktivitas")
        with st.form("form"):
            nama = st.text_input("Nama")
            email = st.text_input("Email")
            umur = st.number_input("Umur", min_value=1, max_value=100)
            divisi = st.selectbox("Divisi", [
                "Commant Center", 
                "DevOps", 
                "Database", 
                "IT Ops XL"
            ])
            aktivitas = st.text_input("Aktivitas")
            layanan = st.text_input("Layanan")
            keterangan = st.text_area("Keterangan")
            rca = st.text_area("Root Cause Analysis (RCA)")
            solusi = st.text_area("Solusi")
            status = st.selectbox("Status", ["Open", "On Progress", "Closed"])
            submitted = st.form_submit_button("Simpan")
            if submitted and nama and email and aktivitas:
                insert_data(nama, email, umur, divisi, aktivitas, layanan, keterangan, rca, solusi, status)
                st.success("Data berhasil ditambahkan!")
    elif menu == "📑 Lihat Data":
        st.header("📑 Data Aktivitas")
        data = fetch_all()
        st.dataframe(data)
    elif menu == "📈 Lihat Data Rekap":
        st.header("📈 Rekap Aktivitas per Divisi")
        df = fetch_all()
        if df.empty:
            st.info("Belum ada data.")
        else:
            rekap = df.groupby("divisi")["status"].value_counts().unstack().fillna(0)
            st.dataframe(rekap)
            st.bar_chart(rekap)
    elif menu == "🔓 Logout":
        st.session_state.logged_in = False
        st.experimental_rerun()
