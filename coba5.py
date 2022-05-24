import pandas as pd


user='akhdan'

ambildatauser = pd.read_csv('userdatabase.csv',index_col = 'username')
dfadu = pd.DataFrame(ambildatauser)
nomor = dfadu.loc['akhdan', 'nomor']

print(nomor)