import pandas as pd
import os
import datetime

filem = input("pilih film = ")
pilihantanggal = int(input('pilih tanggal = '))
pilihanjam = int(input('pilihjam = '))
datakursi2 = pd.read_csv('datakursi2.csv')
carkur3 = pd.DataFrame(datakursi2)
carkur2 = carkur3[carkur3['judul']==filem]
carkur = carkur2[carkur2['tanggal']==pilihantanggal]
indekskursi = carkur[carkur['jam']==pilihanjam].index.item()

datakursi = pd.read_csv('datakursi2.csv', index_col='kode')
dfdk = pd.DataFrame(datakursi)
kursipilihan = input('pilih kursi anda = ')
dfdk.loc[indekskursi, kursipilihan] = 0
dfdk.to_csv("datakursi2.csv")

print(indekskursi)

#datakursi = pd.read_csv('datakursi2.csv', index_col='index')
#dfdk = pd.DataFrame(datakursi)
#kursipilihan = input('pilih kursi anda = ')
#dfdk.loc[indekskursi, kursipilihan] = 0
#dfdk.to_csv("datakursi2.csv")
