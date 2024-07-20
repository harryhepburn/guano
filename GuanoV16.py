import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

def main():
    st.set_page_config(page_title="GUANO Calculator", page_icon="🌴", layout="wide")
    
    st.title("GUANO v1.1")
    st.subheader("Kalkulator Kos Rawatan Ganoderma")

    st.write("""
    ### Kategori Jangkitan Ganoderma:
    - **Kategori A**: Pokok subur, tiada 'frond skirting', masih produktif tetapi TERDAPAT JASAD BERBUAH
    - **Kategori B**: Pokok tidak subur, simptom 'frond skirting', tidak produktif dan TERDAPAT JASAD BERBUAH
    - **Kategori C**: Pokok yang telah tumbang, patah atas atau bawah, mati dan TERDAPAT JASAD BERBUAH
    - **Kategori D**: Pokok samada subur atau tidak subur dengan simptom 'unopen spears (>3fronds)', 'frond skirting' dan pereputan pada pangkal atau atas namun TIADA JASAD BERBUAH
    - **Kategori E**: Pokok Sihat
    - **Kategori F**: Pokok selain kategori di atas, menunjukkan simptom kekurangan nutrien atau 'water stress'
    """)

    st.write("---")

    col1, col2 = st.columns(2)

    with col1:
        nombor_lot = st.text_input("ID Lot")
        serangan_a = st.number_input("Bilangan Pokok Kategori A", min_value=0, value=0)
        serangan_b = st.number_input("Bilangan Pokok Kategori B", min_value=0, value=0)
        serangan_c = st.number_input("Bilangan Pokok Kategori C", min_value=0, value=0)

    with col2:
        serangan_d = st.number_input("Bilangan Pokok Kategori D", min_value=0, value=0)
        serangan_e = st.number_input("Bilangan Pokok Kategori E", min_value=0, value=0)
        serangan_f = st.number_input("Bilangan Pokok Kategori F", min_value=0, value=0)

    pokok_sakit = serangan_a + serangan_b + serangan_c + serangan_d + serangan_f
    sanitasi = serangan_b + serangan_c

    st.write("---")
    st.subheader("Hasil Analisis")
    col3, col4, col5 = st.columns(3)
    col3.metric("Jumlah Pokok Tidak Sihat", pokok_sakit)
    col4.metric("Pokok Memerlukan 'Soil Mounding'", serangan_a)
    col5.metric("Pokok Memerlukan Sanitasi", sanitasi)

    st.write("---")
    st.subheader("Pengiraan Kos")

    cost_a = serangan_a * 15
    cost_b_c = sanitasi * 30
    total_cost = cost_a + cost_b_c

    col6, col7, col8 = st.columns(3)
    col6.metric("Kos 'Soil Mounding'", f"RM {cost_a}")
    col7.metric("Kos Sanitasi Pokok", f"RM {cost_b_c}")
    col8.metric("Jumlah Kos", f"RM {total_cost}")

    st.write("---")
    st.subheader("Anggaran Kerugian Hasil")

    hargaBTS = st.number_input("Harga BTS (RM/MT)", min_value=0.0, value=500.0)
    tahuntuai = st.number_input("Tahun Tuai", min_value=1, max_value=25, value=10)

    kerugian1 = (sanitasi * 0.18) + (serangan_a * 0.8)
    kerugianRM = hargaBTS * kerugian1
    
    col9, col10 = st.columns(2)
    col9.metric("Kerugian Hasil Berat BTS", f"{kerugian1:.2f} MT")
    col10.metric("Kerugian Hasil BTS", f"RM {kerugianRM:.2f}")

    bezarugi = kerugianRM - total_cost
    if kerugianRM > total_cost:
        st.info(f"Jumlah kos adalah kurang daripada kerugian sebanyak RM {bezarugi:.2f}")
    else:
        st.warning(f"Jumlah kos adalah lebih daripada kerugian sebanyak RM {abs(bezarugi):.2f}")

    st.write("---")
    st.subheader("Proyeksi Hasil")

    hasilsemasa = (0.1 * serangan_a) + (0.1 * serangan_d) + (0.18 * serangan_e) + (0.15 * serangan_f)
    st.metric("Hasil Semasa", f"{hasilsemasa:.2f} MT/Tahun")

    dirawat_yield = hasilsemasa
    dibiar_yield = hasilsemasa
    dirawat_reduction = 0.3
    dibiar_reduction = 0.6

    tahuntuai1 = tahuntuai + 1
    years = list(range(tahuntuai1, 26))
    dirawat_yields = []
    dibiar_yields = []

    for year in years:
        dirawat_yield *= (1 - dirawat_reduction)
        dibiar_yield *= (1 - dibiar_reduction)
        dirawat_yields.append(dirawat_yield)
        dibiar_yields.append(dibiar_yield)

    df = pd.DataFrame({
        'Tahun': years,
        'Kawalan (MT)': dirawat_yields,
        'Tiada Kawalan (MT)': dibiar_yields
    })

    st.write(df)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(years, dirawat_yields, label='Kawalan')
    ax.plot(years, dibiar_yields, label='Tiada Kawalan')
    ax.set_xlabel('Tahun')
    ax.set_ylabel('Hasil (MT)')
    ax.set_title('Perbandingan Hasil Antara Kawalan dan Tiada Kawalan')
    ax.legend()

    st.pyplot(fig)

    st.write("---")
    st.success("Terima Kasih Kerana Menggunakan GUANO")

if __name__ == "__main__":
    main()