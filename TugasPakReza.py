Nilai_Tugas = int (input ("Masukkan Nilai Tugas : "))
Uts = int (input ("Masukkan Uts : "))
Uas = int (input ("Masukkan Uas : "))
Kehadiran_Mahasiswa = int (input ("Masukkan Kehadiran_Mahasiswa : "))

Nilai_Akhir = (20/100 * Nilai_Tugas) + (30/100 * Uts) + (50/100 * Uas)

print("Nilai Akhir :" , Nilai_Akhir)
print(Kehadiran_Mahasiswa, "%")

if Nilai_Akhir >= 85 and Kehadiran_Mahasiswa >= 90 and Nilai_Akhir % 2 == 0:
    print("Status       = Lulus Dengan Predikat")
elif Nilai_Akhir >= 75 and Kehadiran_Mahasiswa >= 80:
    print("Status       = Lulus")
else:
    print("Status       = Tidak Lulus")