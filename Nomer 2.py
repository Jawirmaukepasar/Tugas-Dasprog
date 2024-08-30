# Program untuk memperkirakan daya yang dihasilkan oleh bendungan hidroelektrik

# Input dari pengguna
tinggi_bendungan = float(input("Masukkan tinggi bendungan (dalam meter): "))
aliran_air = float(input("Masukkan aliran air (dalam meter kubik per detik): "))

# Menghitung massa air per detik
massa_air = aliran_air * 1000  # dalam kg

# Menghitung kerja yang dilakukan oleh gravitasi (w = mgh)
kerja_gravitasi = massa_air * 9.80 * tinggi_bendungan  # dalam Joule (Watt detik)

# Menghitung daya yang dihasilkan dengan memperhitungkan efisiensi
daya = kerja_gravitasi * 0.90  # dalam Watt

# Mengkonversi daya menjadi megawatt (MW)
daya_mw = daya / 10**6  # konversi dari Watt ke Megawatt

# Menampilkan hasil
print("Daya yang dihasilkan oleh bendungan:", daya_mw, "MegaWatt    ")