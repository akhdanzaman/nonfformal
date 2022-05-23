import datetime
import requests, os, random, time,string
import pandas as pd


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
  
session, user = login()

print(user)
print(user)