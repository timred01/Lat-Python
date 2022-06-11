print("                 TOKO MAINAN ANAK            ")
print("             *************************          ")

#Input Variable
nama    = input('Masukan Nama Pembeli : ')
kode    = input('Masukan Kode Mainan : ')
harga   = int(input('Masukan Harga : '))
jumlah  = int(input('Masukan Jumlah Beli : '))
total   = harga * jumlah
print('')
#Output
print("===================================================")
print("Nama Pembeli = " +nama)
print("Kode Kue     = " +kode)
print("Harga        = " +str(harga))
print("jumlah Beli  = " +str(jumlah))
print("Total        = Rp. " +str(total))
