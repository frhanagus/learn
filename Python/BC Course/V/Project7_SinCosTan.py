import math as m
def sin(degree):
    degree = m.radians(degree)
    hasil = m.sin(degree)
    return hasil

def cos(degree):
    degree = m.radians(degree)
    hasil = m.cos(degree)
    return hasil

def tan(degree):
    degree = m.radians(degree)
    hasil = m.tan(degree)
    return hasil

def sinCosTan():
    while True:
        print("Pilih operasi trigonometri yang ingin dihitung:\n1. Sinus\n2. Cosinus\n3. Tangent\n4. Keluar")
        c = int(input("Masukkan pilihan (1/2/3/4): "))
    
        if c == 1:
            degree = int(input("Masukkan nilai sudut dalam derajat: "))
            hasil = sin(degree)
            print(f"Sinus dari {degree} derajat adalah: {hasil}")
        elif c == 2:
            degree = int(input("Masukkan nilai sudut dalam derajat: "))
            hasil = cos(degree)
            print(f"Kosinus dari {degree} derajat adalah: {hasil}")
        elif c == 3:
            degree = int(input("Masukkan nilai sudut dalam derajat: "))
            hasil = tan(degree)
            print(f"Tangen dari {degree} derajat adalah: {hasil}")
        else:
            print ("Bye bye!")
            break
        
sinCosTan()