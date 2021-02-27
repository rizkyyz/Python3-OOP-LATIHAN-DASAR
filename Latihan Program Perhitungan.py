#Para Ulama ahli fiqih sepakat atas haramnya harta seorang Muslim dan kafir dzimmi.
#Harta mereka tidak boleh direbut, diambil, dicuri, dimakan dengan cara yang tidak dibenarkan 
#syari’at, walaupun sedikit. Allâh Azza wa Jalla berfirman:
#يَا أَيُّهَا الَّذِينَ آمَنُوا لَا تَأْكُلُوا أَمْوَالَكُمْ بَيْنَكُمْ بِالْبَاطِلِ
#Rizkyyz Gans

## INTEGER
print("\nPROGRAM MEMBUAT LUAS BIDANG DATAR")

# mencari luas segitiga
print (" /\  ")
print ("/  \ ","1/2 * alas * tinggi")
print ("----")
print("\nsegitiga")
alas = int(input("masukan nilai alas :"))
tinggi = int(input("masukan nilai tinggi :"))

luas = 0.5*alas*tinggi
print ("luas segitiga :",luas ,"cm")
print ("")
# mencari luas persegi panjang
print (" _______")
print ("|       |")
print ("|_______|")
print ("\nPersegi Panjang")
panjang = int(input("Masukan Nilai Panjang :"))
lebar = int(input("Masukan Nilai Lebar :"))

luas = panjang * lebar
keliling = 2* panjang + lebar

print ("luas persegi panjang :",luas , "cm")
print ("keliling persegi panjang :",keliling ,"cm")
print("")
# persegi 
print (" ____ ")
print ("|    |")
print ("|____|")
print ("\nPERSEGI")
sisi= int(input("Masukan sisi :"))
luas = sisi**2
keliling = 4*sisi

print ("luas persegi     :",luas ,"cm")
print ("Keliling persegi :",keliling ,"cm")
print("")
# Lingkaran
print ("     ..     ")
print ("  .      .  ")
print (" .        . ")
print ("  .      .  ")
print ("     ..     ")
print ("\nLINGKARAN")
r = int(input('masukan jari-jari lingkaran: '))
phi = 3.14
L = phi * (r * r)
print('Luas lingakaran dengan jari-jari {} adalah {}'.format(r, L),"cm")