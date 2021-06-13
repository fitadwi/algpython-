# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 19:12:24 2021

@author: Acer Predator
"""
#nilai total transaksi pembelian printer 
ulang="y"
while ulang=="y" or ulang =="Y":
#Siapkan variabel
    print("===========================")
    print("Pembelian printer")
    print("by Fitaa")
    u=1
    #Hitung
    u =input(" Masukkan Banyak Printer = ")
    n=int(u)
    harga = n * 660000
    print(" Total Harga Pembelian Printer= Rp.",harga)
    ulang = input("\n Ulang program? y/t = ")
    if ulang=="t" or ulang=="T":
        break
