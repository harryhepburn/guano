#!/usr/bin/env python
# coding: utf-8

# In[51]:


print("GUANO v1.1")

print("")
print("Selamat Menggunakan GUANO, Kalkulator Kos Rawatan Ganoderma")


# In[52]:


#Informasi kategori serangan Ganoderma
print("Kategori Jangkitan Ganoderma Adalah Seperti Berikut:")
print("")
print("Kategori A: Pokok subur, tiada 'frond skirting', masih produktif tetapi TERDAPAT JASAD BERBUAH")
print("")
print("Kategori B: Pokok tidak subur, simptom 'frond skirting', tidak produktif dan TERDAPAT JASAD BERBUAH")
print("")
print("Kategori C: Pokok yang telah tumbang, patah atas atau bawah, mati dan TERDAPAT JASAD BERBUAH")
print("")
print("Kategori D: Pokok samada subur atau tidak subur dengan simptom 'unopen spears (>3fronds)', 'frond skirting' dan pereputan pada pangkal atau atas namun TIADA JASAD BERBUAH")
print("")
print("Kategori E: Pokok Sihat")
print("")
print("Kategori F: Pokok selain kategori di atas, menunjukkan simptom kekurangan nutrien atau 'water stress'")
#print("Kategori VP: Tiada pokok")

#Tindakan untuk kategori serangan Ganoderma
#Kategori A: Soil Mounding
#Kategori B, C: Sanitasi
#Kategori D, E, F: Berjaga-jaga

print(" ")
print(" ")


# In[53]:


print("PASTIKAN BANCIAN TELAH DILAKUKAN SEBELUM MENGGUNAKAN APLIKASI INI")


# In[54]:


print(" ")
print("Adakah Anda Ingin Meneruskan GUANO?")
print(" ")
proceed = input(" Tekan Y Untuk Teruskan Dan T Untuk Tamatkan:")

if proceed.upper() == "Y":
    # execute code if user wants to proceed
    print("Terima Kasih. GUANO Memerlukan Input Seterusnya...")
else:
    # execute code if user does not want to proceed
    print("Terima Kasih. Gunakan GUANO Setelah Bancian Dibuat.")
print(" ")


# In[55]:


# Input variables
nombor_lot = input("Masukkan ID Lot: ")
#dirian_pokok = int(input("Masukkan dirian pokok: "))
print("")
serangan_a = int(input("Masukkan Bilangan Pokok Kategori A: "))
print("")
serangan_b = int(input("Masukkan Bilangan Pokok Kategori B: "))
print("")
serangan_c = int(input("Masukkan Bilangan Pokok Kategori C: "))
print("")
serangan_d = int(input("Masukkan Bilangan Pokok Kategori D: "))
print("")
serangan_e = int(input("Masukkan Bilangan Pokok Kategori E: "))
print("")
serangan_f = int(input("Masukkan Bilangan Pokok Kategori F: "))
print("")
print("")
print("")

pokok_sakit = serangan_a + serangan_b + serangan_c + serangan_d + serangan_f
sanitasi = serangan_b + serangan_c

print("Jumlah Pokok Tidak Sihat: ", pokok_sakit)
print("")
print("Pokok Yang Memerlukan 'Soil Mounding' Adalah Sebanyak: ", serangan_a)
print("")
print("Pokok Yang Memerlukan Sanitasi Adalah Sebanyak: ", sanitasi)
print(" ")


# In[57]:


# Calculate cost
print("Kos 'Soil Mounding' adalah RM15/pokok")
print("")
cost_a = (serangan_a) * 15
print("Kos Keseluruhan untuk 'Soil Mounding' adalah sebanyak RM", cost_a)
print("")
print("Kos Sanitasi Pokok adalah RM30/pokok")
print("")
cost_b_c = (serangan_b + serangan_c) * 30
print("Kos Keseluruhan untuk Sanitasi Pokok adalah sebanyak RM", cost_b_c)
print("")
total_cost = cost_a + cost_b_c
print("Jumlah kos yang terlibat adalah RM", total_cost)
print(" ")


# In[58]:


# Pengiraan Kerugian Secara Kasar Setahun
print(" ")
print("Anggaran Kerugian Hasil Disebabkan Ganoderma Tahun Ini")
print(" ")
hargaBTS = int(input("Masukkan Harga BTS (RM/MT): "))
kerugian1 = (sanitasi * 0.18) + (serangan_a * 0.8)
kerugianRM = hargaBTS * kerugian1
print("")
print("Kerugian Hasil Berat BTS: {:.2f}".format(kerugian1), "MT")
print("")
print("Kerugian Hasil BTS: RM {:.2f}".format(kerugianRM))

bezarugi = kerugianRM - total_cost
print("")
if kerugianRM > total_cost:
    print("Jumlah kos adalah kurang daripada kerugian sebanyak RM", bezarugi)
else:
    print("Jumlah kos adalah lebih daripada kerugian sebanyak RM", bezarugi)
    
while True:
    tahuntuai = input("Tahun Tuai: ")
    if tahuntuai.isdigit():
        tahuntuai = int(tahuntuai)
        break
    else:
        print("Masukkan nombor bulat sahaja")

tahunrugi = 25 - tahuntuai
kerugianRM1 = tahunrugi * hargaBTS * (serangan_a * 0.8)
print("")


# In[59]:


#perkiraan hasil tahun tuaian semasa
#Andaian hasil 180kg pada pokok sihat setahun

#Kategori A=0.1 (Kurang 40%)
#Kategori B=0 (Pokok tak berhasil)
#Kategori C=0 (Pokok tak berhasil)
#Kategori D=0.15 (Kurang 20%)
#Kategori E=0.1 (100% hasil)
#Kategori F=0.15 (Kurang 20%)
hasilsemasa = (0.1 * serangan_a) + (0.1 * serangan_d) + (0.18 * serangan_e) + (0.15 * serangan_f)
print(hasilsemasa, "MT/Tahun")


# In[65]:


import matplotlib.pyplot as plt

# Set the initial yield for each plantation
dirawat_yield = hasilsemasa
dibiar_yield = hasilsemasa

# Set the annual reduction rate for each plantation
dirawat_reduction = 0.3
dibiar_reduction = 0.6

# Initialize empty lists to store the yield values for each year
dirawat_yields = []
dibiar_yields = []

# Initialize an empty list to store the table rows
table_rows = []

tahuntuai1 = tahuntuai + 1

# Calculate the yield for each year for both plantations
for year in range(tahuntuai1, 26):
    # Calculate the yield for each plantation in the current year
    dirawat_yield *= (1 - dirawat_reduction)
    dibiar_yield *= (1 - dibiar_reduction)
    
    # Add the yield for each plantation to its respective list
    dirawat_yields.append(dirawat_yield)
    dibiar_yields.append(dibiar_yield)
    
    # Append a row to the table with the current year and yield values
    table_rows.append((year, dirawat_yield, dibiar_yield))

# Print the table
print("Tahun\tKawalan (MT)\tTiada Kawalan (MT)")
for row in table_rows:
    print(f"{row[0]}\t{row[1]:.2f}\t\t{row[2]:.2f}")

# Plot the yield for each year for both plantations on the same graph
plt.plot(range(tahuntuai1, 26), dirawat_yields, label='Kawalan')
plt.plot(range(tahuntuai1, 26), dibiar_yields, label='Tiada Kawalan')

# Add labels and a legend to the graph
plt.xlabel('Tahun')
plt.ylabel('Hasil (MT)')
plt.title('Perbandingan Hasil Antara Kawalan dan Tiada Kawalan')
plt.legend()

# Display the graph
plt.show()


# In[ ]:


#kerugianRM1 = tahunrugi * hargaBTS * (serangan_a * 0.8)
print("")
#print("Kerugian Hasil BTS Sehingga Tanam Semula: RM {:.2f}".format(kerugianRM1))
print("")
#print("Nota: Kiraan tanpa mengambil kira jangkitan baharu kepada pokok sihat dan lain-lain faktor.")
print("")
print("Terima Kasih Kerana Menggunakan GUANO")

