# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 19:42:57 2021

@author: Fitadwi
"""

import os
Clear = lambda : os.system('cls')

jwb = "y"
while jwb=="y" or jwb=="Y": 
    Clear() 
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Daftar Harga Oli Bengkel Motor UD")
    print("by Fitaa ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Pilihan Oli :")
    print("A. Duration SW20 1L")
    print("B. Castrol Magnatec 1L")
    print("C. Federal Supreme XX 1L")
    print("D. Yamalube 1L")
    print("E. Shell 1L")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
    kode = ['a', 'b', 'c', 'd', 'e']
    oli = ['Duration SW20 1L','Castrol Magnatec 1L','Federal Supreme XX 1L','Yamalube 1L',' Shell 1L']
    harga = [53000,50000,54000,45000,46000]
    
    pil = input("Masukkan Pilihan Oli : ")
    
    #identifikasi pilihan
    if pil =="a" or pil =="A" :
        idx = 0
    elif pil =="b" or pil =="B" :
        idx = 1
    elif pil =="c" or pil =="C" :
        idx = 2
    elif pil =="d" or pil =="D" :
        idx = 3
    elif pil =="e" or pil =="E" :
        idx = 4
    else:
        print("Pilihan Salah. Silahkan Masukkan Sesuai Kode!")
        break
    
    #cetak tampilan layar
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Pilihan Oli = ",oli[idx])
    print("Harga       = Rp.",str(harga[idx]))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    #input jumlah oli
    n = input("Masukkan Jumlah Oli yang akan dibeli = ")
    jml = int(n)
    totalA = jml * (harga[idx])
    
    #tahap diskon
    #mendapat diskon 5% apabila pembelian sebelum ppn mencapai minim 200rb
    TotalMinimSebelumppn = 200000 
    if totalA >= TotalMinimSebelumppn : 
        totalB = totalA - totalA*0.05
        print(" ")
        print("Barang mendapat Diskon sebesar 5% !")
    else:
        totalB = totalA

    #Total Biaya Dengan PPN 1%
    totAkhir = totalB + totalB*0.01

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Merek Oli                     =",oli[idx])
    print("Harga Oli                     = Rp.",str(harga[idx]))
    print("Total Barang                  =",jml)
    print("Total Harga (termasuk PPN 1%) = Rp.",str(totAkhir))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    jwb = input("Apakah mau membeli lagi (Y/T) ? ")
    if jwb=="t" or jwb=="T":
        break