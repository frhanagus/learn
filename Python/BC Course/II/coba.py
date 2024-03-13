#2 Mengidentifikasi jenis segitiga
'''
print("Segitiga apakah aku?")

s1, s2, s3 = input("Masukkan panjang ketiga sisi segitiga: ",).split(' ')
sd1, sd2, sd3 = input("Masukkan besar ketiga sudut segitiga \n (dalam derajat): ",).split(' ')

sdt1, sdt2, sdt3 = float(sd1), float(sd2), float(sd3)

if s1 == s2 == s3 and sd1 == sd2 == sd3 == str(60):
    print ("aku segitiga sama sisi")
elif s1 == s2 or s2 == s3 or s1 == s3 and sd1 == sd2 or sd2 == sd3 or sd1 == sd3:
    print ("aku segitiga sama kaki")
elif sdt1 + sdt2 + sdt3 != float(180):
    print ("sudut yang anda masukkan salah:(")
else : print ("aku adalah segitiga sembarang")

#3 Menentukan apakah input adalah tahun kabisat
tahun = int(input("Masukkan Tahun: "))

if tahun%4 == 0 and tahun%100 != 0 or tahun%400 == 0:
    print (f'Tahun', tahun, "adalah tahun kabisat")
else : print (f'Tahun', tahun, "bukanlah tahun kabisat")

#4 Menentukan luas atau keliling persegi panjang
user = input("Pilih 'luas' atau 'keliling': ").lower()

if user == "luas" :
    p = float(input("Masukkan panjang persegi panjang: "))
    l = float(input("Masukkan lebar persegi panjang: "))
    print (f'Luas persegi panjang: ', p*l)
elif user == "keliling" :
    print (f'Keliling persegi panjang: ', 2*(p+l))
    p = float(input("Masukkan panjang persegi panjang: "))
    l = float(input("Masukkan lebar persegi panjang: "))
else : print ("itu tidak ada di pilihan:(")
'''
