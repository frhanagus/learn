#Excercise 1 : Number Guesser
import random 
comp = random.randint(1,20) 
chance = 5

print ('Selamat datang di Game Tebak Angka!')
print (f'Anda memiliki {chance} kesempatan untuk menebak angka antara 1 dan 20\n')
print (f'Kesempatan Anda: {chance}')

tebakan = int(input('Tebak angka: '))
while (True) :
    if tebakan > comp :
        print (f'Angka terlalu tinggi. Coba lagi!')
        chance -= 1
    elif tebakan < comp :
        print (f'Angka terlalu rendah. Coba lagi!')
        chance -= 1
    else : 
        print (f'Selamat, Anda menebak dengan benar!')


