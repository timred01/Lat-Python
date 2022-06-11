'Latihan'
'''Studi Kasus : Pendaftaran Mahasiswa Baru'''

#input mahasiswa baru
NIS     =input("Masukkan NIS : ")
Nama    =input("Masukkan Nama : ")
Kode_Jurusan =input("Masukkan Kode [SI/SIA] : ")

#Proses
if  Kode_Jurusan=="SI" or Kode_Jurusan=="si":
    Nama_Prodi= "Sistem Informasi"
    Harga= "Rp2,400,000"

elif Kode_Jurusan=="SIA" or Kode_Jurusan=="sia":
     Nama_Prodi= "Sistem Informasi Akuntansi"
     Harga= "Rp2,000,000"

else:
    input("Input Salah, Silahkan Ulangi!")
    input("3 ...")
    input("2 ..")
    input("1 .")
    exit()
 
#data mahasiswa baru
print("=============================================")
print("NIS          : ",NIS)
print("Nama         : ",Nama)
print("Kode         : ",Kode_Jurusan)
print("Nama Prodi   : ",Nama_Prodi)
print("Harga        : ",Harga)
print("=============================================")
