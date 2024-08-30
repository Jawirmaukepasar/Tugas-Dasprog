#data si user
skor_yang_diinginkan = input("enter desired grade:")
rata_rata_minimum = float(input("enter minimum average required: "))
rata_rata_saat_ini = float(input("enter current average in course: "))
persentase_final_nilai = float(input("how much percentage the course grade: "))

#Hasil pengurangan 100% - 25%
skor_final_yang_dibutuhkan = (100 - persentase_final_nilai)

#Hasil final nilai yang dibutuhkan
skor_final = (rata_rata_minimum - skor_final_yang_dibutuhkan * rata_rata_saat_ini / 100) * 100 / persentase_final_nilai

print ("skor_yang_kamu_butuhkan", skor_final, "skor_yang_diinginkan", skor_yang_diinginkan)