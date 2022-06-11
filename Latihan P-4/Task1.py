#INPUT DATA KARYAWAN
print("PROGRAM HITUNG GAJI KARYAWAN")
print("===============================")
nama        = input("Nama Karyawan            : ")
jabatan     = input("Golongan Jabatan [1/2/3] : ")
pendidikan  = input("Pendidikan [SMA/D1/S1]   : ")
jam_kerja   = int(input("Jumlah jam kerja         : "))
print("===============================")

#INPUT GAPOK KARYAWAN
gaji = 300000

#PROSES JABATAN
if jabatan=="1":
     persentase="5%"
     tunjangan_jab= 5 * gaji / 100

elif jabatan=="2":
     persentase="10%"
     tunjangan_jab= 10 * gaji / 100

elif jabatan=="3":
     persentase="15%"
     tunjangan_jab= 15 * gaji / 100

else:
    print("Input/Data Salah, Silahkan Ulangi")
    print(" ")
    print(" ")
    exit()

#PROSES PENDIDIKAN
if pendidikan=="SMA" or pendidikan=="sma":
     golongan="2,5%"
     tunjangan_pend=2.5 * gaji / 1000

elif pendidikan=="D1" or pendidikan=="d1":
     golongan="5%"
     tunjangan_pend=5 * gaji / 100

elif pendidikan=="D3" or pendidikan=="d3":
     golongan="20%"
     tunjangan_pend=20 * gaji / 100

elif pendidikan=="S1" or pendidikan=="s1":
     golongan="30%"
     tunjangan_pend=30 * gaji / 100

else:
    print("Input/Data Salah, Silahkan Ulangi")
    print(" ")
    print(" ")
    exit()

#INPUT PERJAM LEMBUR
lembur = 3500

#Proses Jam Kerja
if  jam_kerja >= 8:
    jmlh_jam = (jam_kerja - 8) * lembur

else:
    jmlh_jam = 0

#Output
print("----------------------------------------------------------------")
print("Karyawan yang bernama : "+ (nama))
print("Honor yang di terima")
print(" ")
print("     Tunjangan Jabatan         Rp. ", (tunjangan_jab))
print("     Tunjangan Pendidikan      Rp. ", (tunjangan_pend))
print("     Honor Lembur              Rp. ", (jmlh_jam))
print("     Gaji Pokok                Rp. ", (gaji))
print("                               _____________________+")
total_gaji= int (tunjangan_jab) + int (tunjangan_pend) + int (jmlh_jam) + int (gaji)
print("     Total Gaji                Rp. "+ str (total_gaji))
print("(Gaji Pokok + Tunjangan + Lembur)")
print("----------------------------------------------------------------")
