import streamlit as st

st.title("📚 Aplikasi Ringkasan Materi")

teks = st.text_area("Masukkan Materi:")

if st.button("Ringkas"):
    kalimat = teks.split(".")

    if len(kalimat) >= 2:
        ringkas = kalimat[0] + "." + kalimat[1] + "."
    else:
        ringkas = teks

    st.subheader("Hasil Ringkasan:")
    st.write(ringkas)
