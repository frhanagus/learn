#Project 7 : Parking Machine

hh, mm, ss = input("input in time: ").split(" ")
hh2, mm2, ss2 = input("input out time: ").split(" ")

hh, mm, ss = int(hh), int(mm), int(ss)
hh2, mm2, ss2 = int(hh2), int(mm2), int(ss2)

s = ss2 - ss
m = mm2 - mm
h = hh2 - hh

if s < 0 : 
    s += 60
    m -= 1

if m < 0 : 
    m += 60
    h -= 1

duration = h
if m > 0 or s > 0:
    duration = h + 1

fee = int(duration * 4000)

print(f'in : ',hh, mm, ss)
print(f'out : ',hh2, mm2, ss2)
print(f'duration : ', duration, 'hour')
print(f'Biaya Parkir: ',fee)
