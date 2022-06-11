from math import*           #IMPORT MODUL SEMUA SEKALIGUS

#MODUL PEMANGKATAN
x = int(input("Masukkan bilangan X: "))
y = int(input("Masukkan bilangan Y: "))

pangkat_bilangan = pow(x, y)
print("Hasil dari pemangkatan bilangan tsb adalah : ", pangkat_bilangan)

print("".center(65,"="))

#MODUL FAKTORIAL
angka = int(input("Masukkan bilangan : "))
faktor_bilangan = factorial(angka)
print("Hasil dari Faktorial bilangan tsb adalah : ", faktor_bilangan)

print("".center(65,"="))

#MODUL PENGAKARAN
angka = int(input("Masukkan bilangan : "))
akar_bilangan = sqrt(angka)
print("Akar dari bilangan tsb adalah ", akar_bilangan)