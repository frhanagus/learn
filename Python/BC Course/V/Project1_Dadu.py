import random as r

print ("Selamat datang di Simulasi Permainan Dadu")

def dice_roll():
  return r.randint(1,6)

def condition():

user_input = input("Tekan Enter untuk melempar dadu... ")
while True :
  dice = dice_roll()
  print (f'Anda melempar dadu dan mendapatkan angka: {dice}')
    if dice == 6:
    print ("Anda mendapatkan JACKPOT!\n\nTerima kasih telah bermain!")
    else :
    print ('\nApakah ingin melempar dadu lagi? (ya/tidak):')

# vanno
#Project #1
def LemparDadu():
    import random as r
    print("Selamat datang di Simulasi Permainan Dadu!")
    while True:
        input("Tekan Enter untuk melempar dadu...")
        if True:
            dadu = r.randint(1,6)
            print(f"Anda melempar dadu dan mendapatkan angka: {dadu}")
            if dadu == 6:
                print("Selamat! Anda mendapatkan Jackpot!\nTerima kasih telah Bermain!")
                break
        ask = input("Apakah Anda ingin melempar dadu lagi? (ya/tidak): ")
        ask.lower()
        if ask == "ya":
            True
        else:
            print("Terima kasih telah bermain!")
            break

LemparDadu()