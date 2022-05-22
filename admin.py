import datetime
from datetime import date
import pandas as pd


timenow = datetime.datetime.now()
monthend  = datetime.datetime(timenow.year, timenow.month+1, 1)


def printtanggal(x):
    buattanggal = datetime.datetime(timenow.year,timenow.month,timenow.day+x)
    tanggaltok = buattanggal.day
    return tanggaltok

delta = monthend-timenow



datafilem = pd.read_csv('film.csv')
dfdf = pd.DataFrame(datafilem)
locfilm = dfdf['judul'].tolist()

jadwaljam = ["10","13","16"]


z=0
for judul in range (0,len(locfilm)):
    for i in range (0,delta.days):
        for jam in range (0,len(jadwaljam)):
            
            newschedule = {
                        'index' : [z],
                        'judul' : [locfilm[judul]],
                        'studio' : ['1'],
                        'tanggal' : [printtanggal(i)],
                        'bulan' : [timenow.month],
                        'tahun' : [timenow.year],
                        'jam' : [jadwaljam[jam]],
                        '1' : [1],
                        '2' : [1],
                        '3' : [1],
                        '4' : [1],
                        '5' : [1],
                        '6' : [1],
                        '7' : [1]}
            jadwalfilmbaru = pd.DataFrame(newschedule)
            jadwalfilmbaru.to_csv('datakursi2.csv', mode='a', index=False, header=False)
            z= z+1
            print(z)

print("success")