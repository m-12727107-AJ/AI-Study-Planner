import streamlit as st


def show_study_buddy():
    st.subheader("🤖 AI Study Buddy")

    st.write("Hai! Saya Study Buddy kamu 🌟")
    st.write("Saya boleh beri semangat dan bantu kamu kekal fokus belajar.")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("💪 Beri saya semangat"):
            st.success("Kamu boleh buat! Teruskan sedikit demi sedikit. 🌟")

    with col2:
        if st.button("📚 Tip belajar"):
            st.info("Cuba belajar 25 minit, kemudian rehat 5 minit.")

    st.divider()

    st.write("💬 Mesej untuk Study Buddy")

    message = st.text_input(
        "Tulis mesej kamu:",
        placeholder="Contoh: Saya susah nak fokus..."
    )

    if st.button("🤖 Hantar"):
        if message.strip():
            st.success(
                "Study Buddy: Jangan risau! Kita buat satu langkah pada satu masa. 💛"
            )
        else:
            st.warning("Sila tulis mesej dahulu.")
