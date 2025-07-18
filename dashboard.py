import streamlit as st

def show_dashboard():
    st.title("🧠 Web Command Center")
    st.markdown("## 👋 Selamat Datang di Dashboard Command Center")
    st.success("🚀 *Tetap Semangat, Jangan Menyerah!*")

    st.markdown("---")

    st.subheader("🛡️ Tim Command Center")
    cc_team = [
        "👨‍💻 Andre *'Taulani'*",
        "🧙 Herman *'Syah'*",
        "🦉 Yusuf *'Kala'*",
        "👻 Wahyu *'Sesat'*",
        "🎤 Permadi *'New Daddy'*"
    ]
    for member in cc_team:
        st.markdown(f"- {member}")

    st.markdown("---")

    st.subheader("⚙️ Tim DevOps")
    devops_team = [
        "🧑‍🔧 Junedi *'Anying'*",
        "💻 Aji *'Nomoto'*"
    ]
    for member in devops_team:
        st.markdown(f"- {member}")

    st.markdown("---")

    st.subheader("🗄️ Tim DB")
    db_team = [
        "🎸 Heru *'Roker Dangdut'*",
        "📊 Zaenal *'M'*"
    ]
    for member in db_team:
        st.markdown(f"- {member}")

    st.markdown("---")
    st.info("📌 Gunakan menu di sidebar untuk mulai mencatat aktivitas, lihat rekap, atau update status.")
