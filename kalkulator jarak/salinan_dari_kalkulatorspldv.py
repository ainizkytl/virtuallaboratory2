import streamlit as st

st.set_page_config(page_title="Kalkulator Jarak-Kecepatan-Waktu", layout="centered")

st.title("📏 Kalkulator Jarak - Kecepatan - Waktu")
st.subheader("🧠 Metode Discovery Learning")

st.markdown("""
Masukkan **dua dari tiga** variabel berikut dan kosongkan satu.  
Kalkulator ini akan membantu **menemukan sendiri rumus yang sesuai** dan menghitung hasilnya.
""")

# Input fields
col1, col2, col3 = st.columns(3)
with col1:
    jarak = st.text_input("Jarak (km)", placeholder="Masukkan angka atau kosongkan")
with col2:
    kecepatan = st.text_input("Kecepatan (km/jam)", placeholder="Masukkan angka atau kosongkan")
with col3:
    waktu = st.text_input("Waktu (jam)", placeholder="Masukkan angka atau kosongkan")

# Convert input to float if not empty
def to_float(val):
    try:
        return float(val)
    except:
        return None

d = to_float(jarak)
v = to_float(kecepatan)
t = to_float(waktu)

# Button to calculate
if st.button("🔍 Temukan dan Hitung"):
    known = sum(x is not None for x in [d, v, t])

    if known != 2:
        st.error("❗ Masukkan tepat dua variabel dan kosongkan satu.")
    else:
        st.markdown("---")
        st.subheader("📝 Hasil Penemuan:")

        if d is None:
            d = v * t
            st.write("**Rumus yang digunakan:** Jarak = Kecepatan × Waktu")
            st.success(f"Jarak = {v} × {t} = **{d:.2f} km**")

        elif v is None:
            if t == 0:
                st.error("❌ Waktu tidak boleh 0 saat menghitung kecepatan.")
            else:
                v = d / t
                st.write("**Rumus yang digunakan:** Kecepatan = Jarak ÷ Waktu")
                st.success(f"Kecepatan = {d} ÷ {t} = **{v:.2f} km/jam**")

        elif t is None:
            if v == 0:
                st.error("❌ Kecepatan tidak boleh 0 saat menghitung waktu.")
            else:
                t = d / v
                st.write("**Rumus yang digunakan:** Waktu = Jarak ÷ Kecepatan")
                st.success(f"Waktu = {d} ÷ {v} = **{t:.2f} jam**")
