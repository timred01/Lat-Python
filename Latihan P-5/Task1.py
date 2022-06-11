# Template awal
def menu():
    print("GEROBAK FRIED CHICKEN".center(40, ' '))
    print('-'*40)
    print("Kode     Jenis Potong        Harga")
    print('-'*40)
    print('D        Dada                2500')
    print('P        Paha                2000')
    print('S        Sayap               1500')


#Variabel
jenis_potong = []
kode_potong = []
banyak_potong = []
harga = []
jumlah = []

#Hasil input
def hasil_input():

    i = 0
    while i < banyak_jenis:
        print('Jenis ke \t\t:', i+1)

        kode_potong.append(input('Kode potong D/P/S \t: '))
        banyak_potong.append(int(input('Banyak potong \t\t: ')))

        if kode_potong[i] == 'D' or kode_potong[i] == 'd':
            jenis_potong.append('Dada')
            harga.append('2500')
            jumlah.append(banyak_potong[i] * int('2500'))
        elif kode_potong[i] == 'P' or kode_potong[i] == 'p':
            jenis_potong.append('Paha')
            harga.append('2000')
            jumlah.append(banyak_potong[i] * int('2000'))
        elif kode_potong[i] == 'S' or kode_potong[i] == 's':
            jenis_potong.append('Sayap')
            harga.append('1500')
            jumlah.append(banyak_potong[i] * int('1500'))
        else:
            jenis_potong.append('Kode salah')
            harga.append('0')
            jumlah.append(banyak_potong[i] * int('0'))

        i += 1


def menu_hasil():
    print('')
    print('')
    print('GEROBAK FRIED CHICKEN'.center(60, ' '))
    print('-'*60)
    print('No        Jenis        Harga         Banyak        Jumlah')
    print('          Potong       Satuan        Potong        Harga')
    print('-'*60)

# proses bayar


def bayar():
    jumlah_bayar = 0
    a = 0
    while a < banyak_jenis:
        jumlah_bayar += jumlah[a]
        print('%i         %s         %s          %i             %i' %
              (a+1, jenis_potong[a], harga[a], banyak_potong[a], jumlah[a]))
        a += 1

    print('-'*60)
    pajak = jumlah_bayar * 0.1
    total_bayar = jumlah_bayar + pajak
    print('                          Jumlah bayar           Rp.', jumlah_bayar)
    print('                          Pajak 10%              Rp.', pajak)
    print('                                                 ____________+')
    print('                          Total bayar            Rp.', total_bayar)


# eksekusi
menu()
print('-'*40)
banyak_jenis = int(input("Banyak jenis \t\t: "))
hasil_input()
menu_hasil()
bayar()
