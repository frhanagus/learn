def input_nilai() :
    print ('=== Program Hitung Nilai ===')
    def valid() :
        tugas = int(input("Masukkan nilai Tugas: "))
        UTS = int(input("Masukkan nilai UTS: "))
        UAS = int(input("Masukkan nilai UAS: "))
        if (tugas < 0 and tugas > 100) or (UTS < 0 and UTS > 100) or (UAS < 0 and UAS > 100) :
            print ("Nilai harus berada dalam rentang 0-100, Silakan coba lagi.")
            valid()
        else :
            return tugas, UTS, UAS
    valid()
    return tugas, UTS, UAS

def hitung_nilai() :
    nilai_akhir = (0.15*tugas) + 0.35*UTS + 0.5*UAS
    if nilai_akhir > 80 :
        grade = "A"
    elif nilai_akhir > 70 :
        grade = "B"
    elif nilai_akhir > 60 :
        grade = "C"
    elif nilai_akhir > 50 :
        grade = "D"
    else :
        grade = "E"

    if nilai_akhir >= 60 :
        status = "LULUS"
    else :
        status = "TIDAK LULUS"
    
    return grade, status

def main() :
    input_nilai()
    hitung_nilai()
    print (f'Grade: {grade}')
    print (f'Status: {status}')
    print()

#Vanno
#Project #4: Program Hitung Nilai
def hitung_nilai(tugas, uts, uas):
    nilaiAkhir = tugas*0.15 + uts*0.35 + uas*0.5
    if nilaiAkhir > 80:
        grade = "A"
    elif nilaiAkhir > 70:
        grade = "B"
    elif nilaiAkhir > 60:
        grade = "C"
    elif nilaiAkhir > 50:
        grade = "D"
    else:
        grade = "E"
    if nilaiAkhir < 60:
        status = "Tidak Lulus"
    else:
        status = "Lulus"
    return nilaiAkhir, grade, status

def processing():
    print("="*3 + " Program Hitung Nilai " + "="*3)
    while True:
        while True:
            tugas = int(input("Masukkan nilai Tugas: "))
            uts = int(input("Masukkan nilai UTS: "))
            uas = int(input("Masukkan nilai UAS: "))
            if(tugas in range(0,101) or uts in range(0,101) or uas in range(0,101)):
                break
            else:
                print("Nilai harus di dalam rentang 0-100. Silahkan coba lagi.")
        nilai_akhir, grade, status = hitung_nilai(tugas, uts, uas)
        
        print(f"Nilai akhir: {nilai_akhir}")
        print(f"Grade: {grade}")
        print(f"Status: {status}")
        
        lagi = input("Apakah Anda ingin menghitung nilai lagi? (y/n): ")
        if lagi.lower() != "y":
            break
    
processing()