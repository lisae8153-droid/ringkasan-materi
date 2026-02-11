import streamlit as st

# Judul Web
st.set_page_config(page_title="Asisten Peringkas Materi")

st.title("📘 Asisten Peringkas Materi")
st.write("Masukkan materi, lalu sistem akan membuat ringkasan dalam bentuk paragraf.")

# Input teks
teks = st.text_area("Masukkan Materi di Sini:", height=200)

# Tombol Ringkas
if st.button("Buat Ringkasan"):

    if teks.strip() == "":
        st.warning("⚠️ Materi tidak boleh kosong!")
    else:

        # Pisahkan jadi kalimat
        kalimat = teks.split(".")

        # Ambil maksimal 3 kalimat pertama
        jumlah = min(3, len(kalimat))

        ringkasan = ""

        for i in range(jumlah):
            if kalimat[i].strip() != "":
                ringkasan += kalimat[i].strip() + ". "

        # Output
        st.subheader("Hasil Ringkasan:")
        st.success(ringkasan)
