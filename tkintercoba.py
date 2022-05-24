from tkinter import *
import datetime
import random, string
import pandas as pd
from PIL import ImageTk, Image

root = Tk()
root.title('Aplikasi Booking Tiket Bioskop')
root.geometry('300x400')

def clearscreen():
    e1.grid_forget()
    e2.grid_forget()
    e3.grid_forget()
    e4.grid_forget()
    mylabel1.grid_forget()
    mylabel2.grid_forget()
    mylabel3.grid_forget()
    mylabel4.grid_forget()
    mybutton1.grid_forget()
    mybutton2.grid_forget()

def login():
    userData = pd.read_csv('userdatabase.csv')
    df = pd.DataFrame(userData)
    

    global user
    global pasw
    global nomor
    user=e1.get()
    pasw=e2.get()
 
    matching_creds = (len(df[(df.username == user) & (df.password == pasw)]) > 0)

    if matching_creds:
        print('success')
        session = 1
        clearscreen()
        pilihfilemscreen()
        nomor = df.df['nomor'==user]
        return session, user
    else:
        print('\nYour account is not registered yet!')
        print('please contact admin')
        session = 0
        return session
def register():
    userData = pd.read_csv('userdatabase.csv')
    df = pd.DataFrame(userData)

    global user
    global pasw
    user=e1.get()
    pasw=e2.get()
    namalengkap=e3.get()
    nomor=e4.get()

    matching_creds = (len(df[(df.username == user) ]) < 1 or len(df[(df.nomor == nomor) ]) < 1)

    if matching_creds:
        print('success')
        newuser = {'username' : [user],
                   'password' : [pasw],
                   'namalengkap' : [namalengkap],
                   'nomor' : [nomor]}
        registeruser = pd.DataFrame(newuser)
        registeruser.to_csv('userdatabase.csv', mode='a', index=False, header=False)
        clearscreen()
    else:
        print('Username or number already exist')
        register()
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
def pilihfilem(judulfilmmm):
  global filem,indeksu
  filem = judulfilmmm
  print (indeksfilm(filem))
  indeksu = (indeksfilm(filem))
  movieinfo()
  cariindekskursi()
  pickseat()
  pembayaran()
  rekapbeli()
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
  global indekskursi, pilihanjam,pilihantanggal
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
        global id
        id = id_generator()
        print(id)
        break
        
  return id
def rekapbeli():
    global nomor
    datapembelian = pd.read_csv('datapembelian.csv')
    dfdt = pd.DataFrame(datapembelian)
    ambildatauser = pd.read_csv('userdatabase.csv',index_col = 'username')
    dfadu = pd.DataFrame(ambildatauser)
    nomor = dfadu.loc[user, 'nomor']
    namalengkap = dfadu.loc[user,'namalengkap']
    countrow = dfdt.shape[0]
    nopembelian = f"{(countrow + 1):08d}"
    waktupembelian = datetime.datetime.now()
    
    databelibaru = {'nopembelian' : [nopembelian],
                'waktupembelian' : [waktupembelian],
                'user' : [user],
                'namalengkap' : [namalengkap],
                'nomor' : [nomor],
                'judul' : [filem],
                'waktu' : [pilihanjam],
                'tanggal' : [pilihantanggal],
                'kodebayar' : [id],
                }
    inputdatapembelian = pd.DataFrame(databelibaru)
    inputdatapembelian.to_csv('datapembelian.csv', mode='a', index=False, header=False)

    print('')

def logininstead():
    mybutton1.config(text='Login',
                    command = login)
    mybutton2.config(text='Register instead',
                    command=registerinstead)
    e3.grid_forget()
    e4.grid_forget()
    mylabel3.grid_forget()
    mylabel4.grid_forget()
def registerinstead():
    mybutton1.config(text='Register',
                    command = register)
    mybutton2.config(text='Login instead',
                    command=logininstead)
    mylabel3.grid(row=2,column=0)
    mylabel4.grid(row=3,column=0)
    e3.grid(row=2,column=1)
    e4.grid(row=3,column=1)


def pilihfilemscreen():
    print()
    global img,btnfilm,frame
    frame = Frame(root, width=600, height=400)
    frame.pack()
    frame.place(anchor='center', relx=0.5, rely=0.5)
    image = Image.open("img/4159378067.jpeg")
    
    resize_image = image.resize((100, 100))
    
    img = ImageTk.PhotoImage(resize_image)
    
    btnfilm = Button(image=img, 
                    command=lambda: pilihfilem('kkn'),
                    borderwidth = 0)
    btnfilm.image = img
    btnfilm.pack()
    mylabel1 = Label(root, text=nomor)
    mylabel1.pack()


e1=Entry(root)
e1.grid(row=0,column=1)
e2=Entry(root)
e2.grid(row=1,column=1)
e3=Entry(root)
e3.grid(row=2,column=1)
e4=Entry(root)
e4.grid(row=3,column=1)

mylabel1 = Label(root, text='Username')
mylabel1.grid(row=0,column=0)
mylabel2 = Label(root, text='Password')
mylabel2.grid(row=1,column=0)
mylabel3 = Label(root, text='Nama')
mylabel3.grid(row=2,column=0)
mylabel4 = Label(root, text='Nomor Hp')
mylabel4.grid(row=3,column=0)

mybutton1 = Button(root, 
                text='Register',
                borderwidth=0,
                command=register,
                bg = '#296d98',
                fg = 'white'  )
mybutton1.grid(row=4,column=1)

mybutton2 = Button(root,
                text='Login instead',
                borderwidth = 0,
                command = logininstead)
mybutton2.grid(row=5,column=1)


mainloop()