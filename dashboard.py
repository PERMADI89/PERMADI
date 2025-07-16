import streamlit as st
from database import fetch_all
import pandas as pd
import matplotlib.pyplot as plt

def show_dashboard():
    st.title("📊 Dashboard Statistik")

    data = fetch_all()
    if not data:
        st.info("Belum ada data.")
        return

    df = pd.DataFrame(data, columns=["Nama", "Email", "Umur", "Divisi"])

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Karyawan", len(df))
    col2.metric("Rata-rata Umur", round(df["Umur"].mean(), 1))
    col3.metric("Divisi Terbanyak", df["Divisi"].mode()[0])

    st.markdown("### 📌 Distribusi Umur")
    st.bar_chart(df["Umur"].value_counts().sort_index())

    st.markdown("### 📌 Jumlah Karyawan per Divisi")
    fig, ax = plt.subplots()
    df["Divisi"].value_counts().plot(kind="pie", autopct="%1.1f%%", ax=ax)
    ax.set_ylabel("")
    st.pyplot(fig)
