# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 09:10:12 2021

@author: Acer Predator
"""
#cek kelulusan
import os
Clear = lambda : os.system('cls')

jwb = "y"
while jwb=="y" or jwb=="Y":  
    Clear()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Cek Kelulusan")
    print("by Fitaa")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
    n = int(input("Masukkan Nilai = "))
    #cek nilai
    if int(n)>0 and int(n)<=100:
        if n>60:
            sts = "LULUS"
        else:
            sts = "ULANG"
        print(sts)
    else:
        pesan="Masukkan 0-100 saja"
        print(pesan)
        
    jwb = input("Apakah mau menghitung ulang (Y/T) ? ")
    if jwb=="t" or jwb=="T":
        break