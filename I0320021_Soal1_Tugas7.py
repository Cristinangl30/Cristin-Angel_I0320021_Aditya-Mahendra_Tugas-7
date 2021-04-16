print("PROGRAM MENGGUNAKAN FUNGSI STRING".center(100,("=")))
print("\n")
#Seorang siswa di tugaskan untuk menulis kalimat untuk memberi semangat kepada teman-temannya
text = "hello everyone, happy learning and use your time wisely"
print("Text Awal :", text)
#fungsi replace
str = text.replace("hello","hi")
print("Mengganti Kata Hello =","\n","","","","",str)
#fungsi capitalize()
str = str.capitalize()
print("Mengubah huruf depan jadi Kapital pada awal kalimat  =","\n","","","","",str)
#fungsi center()
str = text.center(80,("*"))
print("Mengisi ruang kiri kanan dengan karakter =","\n","","","","",str)
#Fungsi upper
str = str.upper()
print("Mengubah kalimat jadi kapital =","\n","","","","",str)
#fungsi count
a = text.count('e')
b = text.count('n')
print("jumlah huruf e  = ", a)
print("jumlah huruf n  = ",b)
#fungsi len
print("jumlah karekter = ", len(text))
