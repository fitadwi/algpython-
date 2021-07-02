
"""
Created on Fri Jul  2 19:06:42 2021

Nama  : Fita Dwi Novitasari
Nim   : 20083000003
Kelas : 2A

"""
print("==============================================")
print(" KANTIN FAKULTAS TEKNOLOGI INFORMASI ")
print("==============================================")
print("Menu Makanan")
print("a. Nasi Goreng               15.000")
print("b. Lontong Goreng            14.900")
print("c. Bakso Goreng              12.900")
print("d. Rujak Goreng              13.000")
print("e. Rujak Bakso               15.000")
print("f. Rujak Bakso Pecel         17.000")
print("==============================================")

    #1. siapkan Variabel
kodeMak=['a','b','c','d','e','f']
namaMak=['Nasi Goreng','Lontong Goreng','Bakso Goreng','Rujak Goreng','Rujak Bakso','Rujak Bakso Pecel']
hargaMak=[15000,14900,12900,13000,15000,17000]

kodeMin=['g','h','i','j','k']
namaMin=['Teh Dingin/Hangat/panas','Kopi Dingin','Kopi Teh Panas','Coca Cola Dingin','Coca Cola Panas']
hargaMin=[2500,5000,6500,3500,5000]

    #2.Input makanan
pilihMak = input(">> Masukkan Kode Makanan    = ")
qtyMak   = input(">> Masukkan Jumlah Pesanan  = ")
    
idx = 0;
while idx < len(namaMak):
        #jika value pada list kode[idx] == pilihan
            if kodeMak[idx] == pilihMak:
            #ambil nama barang
                nmbrgMak = namaMak[idx]
            #ambil harga satuan
                hrgsatuanMak = hargaMak[idx]
                print("Makanan             = " + nmbrgMak)
                print("Harga per porsi     = Rp." +    str(format(hrgsatuanMak,',.2f')))
                print("Jumlah yang dipesan = " + qtyMak + " porsi")
                totbyrMak = int(hrgsatuanMak) * int(qtyMak)
           #jika tidak cocok, lanjut ke i berikutnya
            idx = idx + 1      
                
            #4. HITUNG BAYAR    
            jwb = input("Apakah ingin menambah minuman atau makanan ? (Y/T) = ")
            if jwb=="t" or jwb=="T":
                print("==============================================")
                print(" NOTA TRANSAKSI ")
                print("==============================================")
                print(">>> NAMA BARANG      : " + nmbrgMak)
                print(">>> HARGA BARANG     : Rp." +    str(format(hrgsatuanMak,',.2f')))
                print(">>> JUMLAH BARANG    : " + qtyMak)
                print(("-------------------------------"))
                print(">>> TOTAL BAYAR      : Rp." +    str(format(totbyrMak,',.2f')))
                uang = input(">>> UANG             : Rp.")
                x = int(uang)
                kembalian = x - totbyrMak
                print("Kembalian            : Rp."+ str(format(kembalian,',.2f')))

            elif jwb=="y" or jwb=="Y":
                print("==============================================")
                print("Menu Minuman")
                print("g. Teh Dingin/Hangat/panas   2.500")
                print("h. Kopi Dingin               5.000")
                print("i. Kopi Teh Panas            6.500")
                print("j. Coca Cola Dingin          3.500")
                print("k. Coca Cola Panas           5.000")
                print("==============================================")
                #Input minuman
                pilihMin = input(">> Masukkan Kode Minuman    = ")
                qtyMin   = input(">> Masukkan Jumlah Pesanan  = ")
        
            #cek nama minuman
            idx = 0;
            while idx < len(namaMin):
                #jika value pada list kode[idx] == pilihan
                if kodeMin[idx] == pilihMin:
                    #ambil nama barang
                    nmbrgMin = namaMin[idx]
                    #ambil harga satuan
                    hrgMin = hargaMin[idx]
                    print("Makanan             = " + nmbrgMin)
                    print("Harga per porsi     = Rp." + str(format(hrgMin,',.2f')))
                    print("Jumlah yang dipesan = " + qtyMin )
           #jika tidak cocok, lanjut ke i berikutnya
                idx = idx + 1    
            totbyrMin = int(hrgMin) * int(qtyMin)
            total = totbyrMak + totbyrMin
            #Menampilkan pembelanjaan
            print("==============================================")
            print(" NOTA TRANSAKSI ")
            print("==============================================")
            print(">>> NAMA BARANG      : " + nmbrgMak + "; " + nmbrgMin)
            print(">>> HARGA BARANG     : Rp." + str(format(hrgsatuanMak,',.2f')) + "; Rp. " + str(format(hrgMin,',.2f')))
            print(">>> JUMLAH BARANG    : " + qtyMak + "; " + qtyMin )
            print(("-------------------------------"))
            print(">>> TOTAL BAYAR      : Rp." + str(format(total,',.2f')))
            uang = input(">>> UANG             : Rp.")
            x = int(uang)
            kembalian = x - total
            print("Kembalian            : Rp."+ str(format(kembalian,',.2f')))
            break
       
