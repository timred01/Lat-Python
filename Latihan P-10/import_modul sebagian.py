from math import pow                #INI CONTOH IMPORT MODUL SEBAGIAN
from math import factorial          #INI CONTOH IMPORT MODUL SEBAGIAN

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