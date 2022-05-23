from tkinter import *
import datetime
import random, string
import pandas as pd

root = Tk()
root.title('Aplikasi Booking Tiket Bioskop')
root.geometry('300x400')


pilihanfilm = ''
indekss = ""
user = ""
nomor = ""
waktu = ""
tanggal = ""
kodebayar = ""
session = 0



def login():
  userData = pd.read_csv('userdatabase.csv')
  df = pd.DataFrame(userData)

  print('Login Tools\n')
  user = input('Username : ')
  pasw = input('Password : ')
  
  matching_creds = (len(df[(df.username == user) & (df.password == pasw)]) > 0)

  if matching_creds:
    print('success')
    session = 1
    return session, user,
  else:
    print('\nYour account is not registered yet!')
    print('please contact admin')
    session = 0
    return session

def register():
    userData = pd.read_csv('userdatabase.csv')
    df = pd.DataFrame(userData)

    user = input('Username : ')
    pasw = input('Password : ')
    namalengkap = input('Nama Lengkap : ')
    nomor = input('Nomor Telepon : ')


    matching_creds = (len(df[(df.username == user) ]) < 1 or len(df[(df.nomor == nomor) ]) < 1)

    if matching_creds:
        print('success')
        newuser = {'username' : [user],
                   'password' : [pasw],
                   'namalengkap' : [namalengkap],
                   'nomor' : [nomor]}
        registeruser = pd.DataFrame(newuser)
        registeruser.to_csv('userdatabase.csv', mode='a', index=False, header=False)
    else:
        print('Username or number already exist')
        register()

while session != 0:
  
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
  def pilihfilem():
    filem = input('Film : ')
    print (indeksfilm(filem))
    indeksu = (indeksfilm(filem))
    return indeksu,filem
  def movieinfo():
    daftarfilm = pd.read_csv('film.csv')
    df = pd.DataFrame(daftarfilm)
    
    judul= (df['judul'].iloc[indeksu])
    harga = (df['harga'].iloc[indeksu])
    durasi = (df['durasi'].iloc[indeksu])
    
    fullinfo = '''
    Judul film \t\t : {0}
    Harga Tiket \t : {1}
    Durasi film\t\t : {2}
    '''
    print(fullinfo.format(judul,harga,durasi))
  def cariindekskursi():
    pilihantanggal = int(input('pilih tanggal = '))
    pilihanjam = int(input('pilihjam = '))
    datakursi2 = pd.read_csv('datakursi2.csv')
    carkur3 = pd.DataFrame(datakursi2)
    carkur2 = carkur3[carkur3['judul']==filem]
    carkur = carkur2[carkur2['tanggal']==pilihantanggal]
    indekskursi = carkur[carkur['jam']==pilihanjam].index.item()
    return indekskursi,pilihanjam,pilihantanggal
  def availableseat():
      kursifilm = pd.read_csv('datakursi2.csv')
      dfkf = pd.DataFrame(kursifilm)
      locfilm = dfkf.loc[indekskursi]
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
    availableseat()
    datakursi = pd.read_csv('datakursi2.csv', index_col='kode')
    dfdk = pd.DataFrame(datakursi)
    kursipilihan = input('pilih kursi anda = ')
    dfdk.loc[indekskursi, kursipilihan] = 0
    dfdk.to_csv("datakursi2.csv")
    return kursipilihan
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
          print(id)
          break
          
    return id
  def rekapbeli():
      datapembelian = pd.read_csv('datapembelian.csv')
      dfdt = pd.DataFrame(datapembelian)

      countrow = dfdt.shape[0]
      nopembelian = f"{(countrow + 1):08d}"
      waktupembelian = datetime.datetime.now()
      
      databelibaru = {'nopembelian' : [nopembelian],
                  'waktupembelian' : [waktupembelian],
                  'user' : [user],
                  'nomor' : [nomor],
                  'judul' : [filem],
                  'waktu' : [pilihanjam],
                  'tanggal' : [pilihantanggal],
                  'kodebayar' : [kodebayar],
                  }
      inputdatapembelian = pd.DataFrame(databelibaru)
      inputdatapembelian.to_csv('datapembelian.csv', mode='a', index=False, header=False)

      print('')
  
  


def kliked():
    mylabel4 = Label(root, text=e.get())
    mylabel4.pack()


e=Entry(root)
e.pack()

mylabel = Label(root, text='ini label 1')
mylabel.pack()


mybutton = Button(root, 
                text='Ini button',
                borderwidth=0,
                command=kliked,
                bg = '#296d98',
                fg = 'white'  )
mybutton.pack()

mainloop()