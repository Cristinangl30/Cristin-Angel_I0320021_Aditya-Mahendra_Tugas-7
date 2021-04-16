print("PROGRAM MENGGUNAKAN FUNGSI NUMERIK".center(100,("=")))

nilai_Mahasiswa = input("Masukkan nilai Mahasiswa (pisahkan dengan spasi) : ").split()

for i in range(len(nilai_Mahasiswa)):
    #Konversi ke int
    nilai_Mahasiswa[i] = int(nilai_Mahasiswa[i])

#Mencari rata-rata nilai
rerata = sum(nilai_Mahasiswa)/len(nilai_Mahasiswa)

print("Nilai yang diinput : ", nilai_Mahasiswa)
print('\n')

import math
#Fungsi Max = nilai tertinggi
print("Nilai yang paling tinggi adalah ", max(nilai_Mahasiswa))

#Fungsi Min =  nilai terendah
print("Nilai yang paling rendah adalah ", min(nilai_Mahasiswa))

print("Rata-rata nilai mahasiswa adalah ", rerata)
#Fungsi ceil = pembulatan ke atas
print("Rata-rata nilai dengan pembulatan ke atas adalah ", math.ceil(rerata))

#Fungsi floor = pembulatan ke bawah
print("Rata-rata nilai dengan pembulatan ke bawah adalah ", math.floor(rerata))