import datetime
import requests, os, random, time,string
import pandas as pd

pilihanfilm = ''
indekss = ""
user = ""
nomor = ""
waktu = ""
tanggal = ""
kodebayar = ""


def login():
  userData = pd.read_csv('userdatabase.csv')
  df = pd.DataFrame(userData)

  print('Login Tools\n')
  user = input('Username : ')
  pasw = input('Password : ')
  
  matching_creds = (len(df[(df.username == user) & (df.password == pasw)]) > 0)

  if matching_creds:
    print('success')
  else:
    print('\nYour account is not registered yet!')
    print('please contact admin')

def register():
    userData = pd.read_csv('userdatabase.csv')
    df = pd.DataFrame(userData)

    user = input('Username : ')
    pasw = input('Password : ')

    matching_creds = (len(df[(df.username == user) ]) < 1)

    if matching_creds:
        print('success')
        newuser = {'username' : [user],
                   'password' : [pasw]}
        registeruser = pd.DataFrame(newuser)
        registeruser.to_csv('userdatabase.csv', mode='a', index=False, header=False)
    else:
        print('Username already exist')
        register()


def inputfilm():
    filem = input('Film : ')
    return filem


def movieinfo():
    daftarfilm = pd.read_csv('film.csv')
    df = pd.DataFrame(daftarfilm)



    judul= (df['judul'].iloc[pilihfilm()])
    harga = (df['harga'].iloc[pilihfilm()])
    durasi = (df['durasi'].iloc[pilihfilm()])
    
    fullinfo = '''
    Judul film \t\t : {0}
    Harga Tiket \t : {1}
    Durasi film\t\t : {2}
    '''
    print(fullinfo.format(judul,harga,durasi)
    )


def indeksfilm(x):
  daftarfilm = pd.read_csv('film.csv')
  df = pd.DataFrame(daftarfilm)
  
  pilihanfilm = x
  
  matching_creds = (len(df[(df.judul == pilihanfilm)]) > 0)

  if matching_creds:
    indekss = df[df['judul']==pilihanfilm].index.item()
    return indekss
  else:
    print()


print (indeksfilm(filem))
indeksu = (indeksfilm(filem))


def pilihfilm():
  daftarfilm = pd.read_csv('film.csv')
  df = pd.DataFrame(daftarfilm)


  
  judul= (df['judul'].iloc[indeksu])
  harga = (df['harga'].iloc[indeksu])
  durasi = (df['durasi'].iloc[indeksu])
  
  fullinfo = '''
  Judul film \t\t : {0}
  Harga Tiket \t\t : {1}
  Durasi film\t\t : {2}
  '''
  print(fullinfo.format(judul,harga,durasi))
  

def availableseat():
    kursifilm = pd.read_csv('datakursi2.csv')
    dfkf = pd.DataFrame(kursifilm)
    locfilm = dfkf.loc[indeksu]
    daftarkursi = locfilm.tolist()
    print()
    for a in range (7,len(daftarkursi)):
        if daftarkursi[a] == 1:
            print('%d Available'%(a-6))
        else:
            print('%d Booked' %(a-6))
    print()


def pickdate():
  print()
  time = datetime.datetime.now()


def pickseat():
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



def konfrimasi():
  print()

def id_generator(size=15, chars=string.ascii_uppercase + string.digits):
  return ''.join(random.choice(chars) for _ in range(size))

def pembayaran():
  datapembelian = pd.read_csv('datapembelian.csv')
  dfdp = pd.DataFrame(datapembelian)
  while True:
    id_generator()
    if (len(dfdp.loc[dfdp['kodebayar'] == id_generator])) < 1:
        id = id_generator()
        break
        
  print("Kode bayar")
  print(id)

def rekapbeli():
    nopembelian = 0
    
    userData = pd.read_csv('userdatabase.csv')
    dfud = pd.DataFrame(userData)
    datafilm = pd.read_csv('film.csv')
    dfdfi = pd.DataFrame(datafilm)
    datakursi = pd.read_csv('datakursi2.csv')
    dfdk = pd.DataFrame(datakursi)
    datapembelian = pd.read_csv('datapembelian.csv')
    dfdt = pd.DataFrame(datapembelian)

    countrow = dfdt.shape[0]
    nopembelian = print(f"{(countrow + 1):08d}")

    databelibaru = {'nopembelian' : [nopembelian],
                'user' : [user],
                'nomor' : [nomor],
                'judul' : [pilihanfilm],
                'waktu' : [waktu],
                'tanggal' : [tanggal],
                'kodebayar' : [kodebayar],
                }
    inputdatapembelian = pd.DataFrame(databelibaru)
    inputdatapembelian.to_csv('datapembelian.csv', mode='a', index=False, header=False)

    print('')
