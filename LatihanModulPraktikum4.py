# Buat list dengan 5 elemen
a = [1,3,5,7,9]

# Akses List
## Tampilkan elemen ke 3
print(a[2])
## Ambil nilai elemen ke 2 sampai ke 4
print(a[1:4])
## Ambil elemen terakhir
print(a[4])

# Ubah elemen list
## Ubah elemen ke 4 dengan nilai lainnya
a[3] = 11

## Ubah elemen ke 4 sampai dengan elemen terakhir
a[3:5] = 33, 55
print(a)

# Tambah elemen list
## Ambil 2 bagian dari list pertama (A) untuk dan jadikan list kedua (B)
b = (a[0:2])
## Tambah list B dengan nilai string
b.append("Indonesia")
## Tambah List B dengan 3 nilai
b.extend([66,77,88])
print(b)
## Gabungkan list B dengan list A
c = a + b
print(c)