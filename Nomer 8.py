import math
#berapa biaya yg di perlukan dan air yang dapat di hemat dalam suatu populasi
#toilet lama = 15 liter / flush
#toilet baru = 2 liter / flush
#maka total air yang di hemat adalah 13 liter / flush
#terdapat 1 toilet untuk 3 orang
#rata rata perhari sebanyak 14 kali flush / toilet
#biaya untuk mengganti toilet adalah 150$
#toilet baru memperlukan 14 liter perhari dengan anggapan rata-rata perhari adalah 14 flush
#1. Asumsi semua orang pakai toilet  jadi ada 4 orang berarti 2 toilet terpakai (3 1)

populasi = int(input("populasi yang ada: "))

jumlah_toilet = math.ceil(populasi/3)

magnitude = jumlah_toilet * 28
cost = jumlah_toilet * 150

print("jumlah air yang di perlukan adalah", magnitude, "liter dan harga yang di butuhkan adalah", cost,"$")