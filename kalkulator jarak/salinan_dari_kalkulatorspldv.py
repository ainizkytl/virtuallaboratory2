import streamlit as st

def calculate_unknown(distance=None, speed=None, time_val=None):
    """Menghitung nilai yang tidak diketahui berdasarkan dua nilai yang diberikan."""
    if distance is None and speed is not None and time_val is not None:
        return "Jarak", speed * time_val
    elif speed is None and distance is not None and time_val is not None:
        return "Kecepatan", distance / time_val
    elif time_val is None and distance is not None and speed is not None:
        return "Waktu", distance / speed
    else:
        return None, None # Kondisi tidak valid (kurang dari 2 nilai atau 3 nilai diberikan)

st.set_page_config(
    page_title="Kalkulator Jarak, Kecepatan, Waktu (Discovery Learning)",
    page_icon="⏱️",
    layout="centered"
)

st.title("Kalkulator Perbandingan Jarak, Kecepatan, dan Waktu")
st.markdown("---")

st.write(
    "Selamat datang di Kalkulator Perbandingan Jarak, Kecepatan, dan Waktu! "
    "Aplikasi ini dirancang untuk membantu Anda memahami hubungan antara ketiga konsep ini "
    "melalui metode **Discovery Learning**."
)
st.write(
    "Anda akan memasukkan **dua dari tiga nilai** (Jarak, Kecepatan, Waktu), dan aplikasi akan menghitung nilai yang tidak diketahui. "
    "Perhatikan bagaimana perubahan satu nilai memengaruhi nilai lainnya."
)

st.markdown("---")
st.header("Skenario Eksplorasi")

# Menggunakan input numerik dengan nilai default None
distance_input = st.number_input("Masukkan **Jarak** (km), atau biarkan kosong (0 untuk kosong):", min_value=0.0, format="%.2f")
speed_input = st.number_input("Masukkan **Kecepatan** (km/jam), atau biarkan kosong (0 untuk kosong):", min_value=0.0, format="%.2f")
time_input = st.number_input("Masukkan **Waktu** (jam), atau biarkan kosong (0 untuk kosong):", min_value=0.0, format="%.2f")

# Konversi 0 menjadi None untuk logika perhitungan
distance = distance_input if distance_input > 0 else None
speed = speed_input if speed_input > 0 else None
time_val = time_input if time_input > 0 else None

provided_count = sum(x is not None for x in [distance, speed, time_val])

if st.button("Hitung!"):
    if provided_count != 2:
        st.error("Anda harus memasukkan tepat **dua nilai** (lebih besar dari 0) untuk menghitung yang ketiga. Silakan coba lagi.")
    else:
        unknown_var, result = calculate_unknown(distance, speed, time_val)

        if unknown_var:
            st.subheader("Hasil Perhitungan:")
            if distance is not None:
                st.write(f"**Jarak:** {distance:.2f} km")
            if speed is not None:
                st.write(f"**Kecepatan:** {speed:.2f} km/jam")
            if time_val is not None:
                st.write(f"**Waktu:** {time_val:.2f} jam")

            st.success(f"Nilai yang dihitung ({unknown_var}): **{result:.2f}**")
            st.info("💡 Renungkan: Bagaimana perubahan input Anda memengaruhi hasil?")
        else:
            st.warning("Terjadi kesalahan dalam perhitungan. Pastikan Anda memasukkan dua nilai yang valid.")

st.markdown("---")
st.write("Semoga Anda mendapatkan pemahaman yang lebih baik tentang hubungan J-K-W melalui eksplorasi ini!")
st.markdown("Dibuat dengan ❤️ yuniraraaini.")
