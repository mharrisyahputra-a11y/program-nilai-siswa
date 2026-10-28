nama = input("Masukkan nama siswa: ")
nilai = int(input("Masukkan nilai siswa: "))

lulus = nilai >= 75

if lulus == True:
    print("Nama siswa:", nama)
    print("Nilai:", nilai)
    print("Status: LULUS")
else:
    print("Nama siswa:", nama)
    print("Nilai:", nilai)
    print("Status: TIDAK LULUS")