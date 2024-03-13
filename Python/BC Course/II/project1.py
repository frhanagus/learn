#Project 1 : Shopping Cart

Pilih = int(input("Mau Buah apa 1)Apple, 2)Banana, 3)Orange, 4)Grapes: ").lower())

if Pilih == int(1):
    price = float(1.00)
    print ("kamu memilih Apple")
elif Pilih == int(2):
    price = float(0.75)
    print ("kamu memilih Banana")
elif Pilih == int(3):
    price = float(1.25)
    print ("kamu memilih Orange")
elif Pilih == int(4):
    price = float(2.50)
    print ("kamu memilih Grapes")
else : print ("Buah tidak ada")

qty = int(input("Berapa banyak?"))

sum = float(price*qty)

print ("jumlah yang harus dibayar : $", sum)
