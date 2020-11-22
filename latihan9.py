print(":***********:")
print("nama     : Antini permatasari")
print("NIM      : 312010095")
print("kelas    : TI.20.B.1")
print(":**********:")


# list indexeng
print("Buatlah sebuah list sebanyak 5 elemen dengan nilai bebas")
list_saya = ['1', '2', '3', '4', '5']
print(list_saya)

# output: 3
print("tampilkan elemen ke 3")
print(list_saya[2])

# mengambil list
print("Ambil nilai elemen ke 2 sampai elemen ke 4")
print(list_saya[1:4])

# ambil elemen terakhir
print("Ambil elemen terakhir")
print(list_saya[4])

# ubah elemen list
print("Ubah elemen ke4 dengan nilai lainnya")
list_saya [3]=8
print(list_saya[3])
print("Ubah elemen ke 4 sampai dengan elemen terakhir")
list_saya [4:5] = [16,28]
print(list_saya)

# tambah elemen list
print("Ambil 2 bagian dari list pertama (A) dan jadikan list ke 2 (B)")
list_kamu = list_saya [3:4]
print(list_kamu[:2])

print("Tambah list B dengan nilai string")
list_kamu.append("Antini")
print(list_kamu)

print("Tambah list B dengan 3 nilai")
list_kamu.append(["Antini_permatasari",3,2])
print(list_kamu)

print("Gabungkan list B dengan list A")
gabung=list_saya,list_kamu
print(gabung)

