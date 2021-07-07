# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 12:42:06 2021

NAMA    : FITA DWI NOVITASARI
NIM     : 20083000003
KELAS   :2A
"""

import os
import sys
import datetime
from time import process_time_ns

x = datetime.datetime.now()

gol = [1,2,3]
gaji_p = [2500000,4500000,6500000]
os.system('cls')
print("="*60)
print(" "*12,"PERHITUNGAN GAJI KARYAWAN CV.LOGOS")
print("             Tanggal : ",x.strftime("%x"))
print("="*60)
print(" "*2,"!!! DIMOHON KARYAWAN CV.LOGOS MENGISI DATA DIBAWAH !!!")

nama =         input("NAMA                 :" + " "*2)
golongan = int(input("golongan             :" + " "*2))
jk =           input("JENIS KELAMIN (L/P)  :" + " "*2)
sk =           input("STATUS KAWIN         :" + " "*2)
ja =       int(input("JUMLAH ANAK          :" + " "*2))
os.system('cls')
if golongan == 1:
	i = 0
	tun = 0.01
elif golongan == 2:
	i = 1
	tun = 0.03
elif golongan == 3:
	i = 2
	tun = 0.05
if jk.upper() == "L" and sk.lower() == 'kawin':
	tun_istri = gaji_p[i]*tun
else : tun_istri = 0
if sk.lower() == 'kawin' and ja > 0:
	tun_anak = gaji_p[i] * 0.02
else: tun_anak = 0
gaji_brt = gaji_p[i] + tun_anak + tun_istri
biaya_jbtn = gaji_brt * 0.005
iuran_p = 15000
iuran_o = 3500
gaji_net = gaji_brt - biaya_jbtn - iuran_o - iuran_p
print(" ")

print(" ")
print("="*40)
print(" "*10,"SLIP GAJI")
print(" "*10,"Tanggal : ",x.strftime("%x"))
print("="*40)
print(" ")
print(" ")
print("Nama                 :"," ",nama)
print("Golongan             :"," ",golongan)
print("Jenis Kelamin        :"," ",jk)
print("Status Kawin         :"," ",sk)
print("Gaji Pokok           :"," ",gaji_p[i])
print("Tunjangan Istri      :"," ",tun_istri)
print("Tunjangan Anak       :"," ",tun_anak)
print(">>Gaji Bruto         :"," ",gaji_brt)
print("-"*22)
print("Biaya Jabatan        :"," ",biaya_jbtn)
print("Iuran Pensiun        :"," ",iuran_p)
print("Iuran Organisasi     :"," ",iuran_o)
print(">>Gaji Netto         :"," ",gaji_net)