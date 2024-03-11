PB1, LB1, PS1, LS1 = input("Silahkan masukkan panjang dan lebar bangunan dan sekolah 1: ").split(' ')
PB1, LB1, PS1, LS1 = int(PB1), int(LB1), int(PS1), int(LS1)

PB2, LB2, PS2, LS2 = input("Silahkan masukkan panjang dan lebar bangunan dan sekolah 2: ").split(' ') 
PB2, LB2, PS2, LS2 = int(PB2), int(LB2), int(PS2), int(LS2)

PB3, LB3, PS3, LS3 = input("Silahkan masukkan panjang dan lebar bangunan dan sekolah 3: ").split(' ') 
PB3, LB3, PS3, LS3 = int(PB3), int(LB3), int(PS3), int(LS3)

#Hitung Luas Tanah Sekolah
LuasSekolah1 = PS1*LS1
LuasSekolah2 = PS2*LS2
LuasSekolah3 = PS3*LS3

#Hitung Luas Bangunan Sekolah
LuasBangunan1 = PB1*LB1
LuasBangunan2 = PB2*LB2
LuasBangunan3 = PB3*LB3

#Luas Taman Sekolah 
LuasTaman1 = LuasSekolah1 - LuasBangunan1
LuasTaman2 = LuasSekolah2 - LuasBangunan2
LuasTaman3 = LuasSekolah3 - LuasBangunan3

#Total Taman dari 3 sekolah
sumT = LuasTaman1 + LuasTaman2 + LuasTaman3

print("Luas total taman di 3 sekolah adalah: ", sumT)