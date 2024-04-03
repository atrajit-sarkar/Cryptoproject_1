from Affinecipher.dict import *
from Harrycipher.coverstion import conv

def encrypt(message,key):
  en=[]
  key=list(key)
  lis=list(message)
  for i in range(len(lis)):
    if get_key(lis[i]) is not None:
     en.append(dict[(int(key[0]) * get_key(lis[i]) + int(key[1])) % 40])
    else:
      print("Error occured")
  
  return conv(en)
  