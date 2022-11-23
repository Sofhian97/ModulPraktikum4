list_mahasiswa = []
while True:
    nama = input("Nama : ")
    NIM = int(input("NIM : "))
    tugas = int(input("Nilai Tugas : "))
    uts = int(input("Nilai UTS : "))
    uas = int(input("Nilai UAS : "))
    akhir = (float(tugas * 0.3) + (uts * 0.35) + (uas * 0.35))

    DataMahasiswa = [nama, NIM, tugas, uts, uas, akhir]
    list_mahasiswa.append(DataMahasiswa)

    TambahData = (input("Tambah Data? (y/t)"))
    if TambahData == "y" :
        continue

    print("="*72)
    print("No\t|","\t\t\tNama\t\t  |","\tNIM   |","Tugas |","UTS |","UAS |","Akhir |")
    for nomor,mahasiswa in enumerate (list_mahasiswa) :
        print(f"{nomor+1}\t| {mahasiswa[0]} |\t{mahasiswa[1]} |   {mahasiswa[2]}  |  {mahasiswa[3]} |  {mahasiswa[4]} | {mahasiswa [5]} |")
    print("="*72)
    if TambahData == "t" :
            break





