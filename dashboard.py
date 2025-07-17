import streamlit as st
from database import fetch_all
import pandas as pd

def show_dashboard():
    st.title("📊 Dashboard Statistik")

    df = fetch_all()
    if df.empty:
        st.info("Belum ada data.")
        return

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Entri", len(df))
    col2.metric("Rata-rata Umur", round(df["umur"].mean(), 1))
    col3.metric("Status Terbanyak", df["status"].mode()[0])

    st.markdown("### 📌 Jumlah per Divisi")
    st.bar_chart(df["divisi"].value_counts())

    st.markdown("### 📌 Status Permasalahan")
    st.bar_chart(df["status"].value_counts())
