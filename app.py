import streamlit as st
from auth import check_login
from dashboard import show_dashboard
from database import init_db, insert_data, fetch_all, update_status
import pandas as pd

st.set_page_config(page_title="Admin Dashboard Extended", layout="wide")
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
            st.session_state.username = username
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
            nama = st.selectbox("Nama", [st.session_state.username])
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
            if submitted and email and aktivitas:
                insert_data(nama, email, umur, divisi, aktivitas, layanan, keterangan, rca, solusi, status)
                st.success("Data berhasil ditambahkan!")

    elif menu == "📑 Lihat Data":
        st.header("📑 Data Aktivitas")
        data = fetch_all()
        df = pd.DataFrame(data, columns=[
            "Tanggal", "Nama", "Email", "Umur", "Divisi", "Aktivitas", 
            "Layanan", "Keterangan", "RCA", "Solusi", "Status"
        ])
        for i, row in df.iterrows():
            with st.expander(f"{row['Nama']} - {row['Email']}"):
                st.write(row.drop("Status"))
                new_status = st.selectbox(
                    "Update Status", 
                    ["Open", "On Progress", "Closed"], 
                    index=["Open", "On Progress", "Closed"].index(row["Status"]),
                    key=f"status_{i}"
                )
                if st.button("Update", key=f"update_{i}"):
                    update_status(row["Email"], new_status)
                    st.success("Status berhasil diperbarui!")
                    st.experimental_rerun()

    elif menu == "📈 Lihat Data Rekap":
        st.header("📈 Rekap Aktivitas per Divisi")
        data = fetch_all()
        df = pd.DataFrame(data, columns=[
            "Tanggal", "Nama", "Email", "Umur", "Divisi", "Aktivitas", 
            "Layanan", "Keterangan", "RCA", "Solusi", "Status"
        ])
        rekap = df.groupby("Divisi")["Status"].value_counts().unstack().fillna(0)
        st.dataframe(rekap)
        st.bar_chart(rekap)

    elif menu == "🔓 Logout":
        st.session_state.logged_in = False
        st.experimental_rerun()
