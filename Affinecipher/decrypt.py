from Affinecipher.inverse import inverse
from Affinecipher.dict import *
def decryption(message,key):
  message=message.upper()
  a=inverse(int((key[0])))
  str=""
  for i in message:             
    x=get_key(i)
    x=(a*x-a*int(key[1]))%41
    str=str+dict[x]
    
  return str.capitalize()